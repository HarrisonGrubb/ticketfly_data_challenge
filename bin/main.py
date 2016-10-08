#!/usr/bin/env python
"""
coding=utf-8

Response to Ticketfly data challenge

"""
import logging

import numpy as np
import pandas as pd
import patsy
import statsmodels.api as sm

logging.basicConfig(level=logging.DEBUG)


def create_training_df():
    """
    Read in tables from file, and join them to create a single observation table
    :return:
    """

    # Read in tables from CSV
    email_df = pd.read_csv('../data/input/email_table.csv')
    email_opened_df = pd.read_csv('../data/input/email_opened_table.csv')
    link_df = pd.read_csv('../data/input/link_clicked_table.csv')

    # Perform joins to create one observations df
    observation_df = pd.merge(email_df, email_opened_df, on='email_id')
    observation_df = pd.merge(observation_df, link_df, on='email_id')

    # Feature typing
    observation_df['opened_flag'] = observation_df['opened_flag'] == 'Yes'
    observation_df['CTA_link_click'] = observation_df['CTA_link_click'] == 'Yes'
    observation_df['row_weight'] = 1

    logging.info('Observation dataframe columns: \n%s' % observation_df.columns)
    logging.info('Observation dataframe shape: \n%s' % str(observation_df.shape))
    logging.info('Observation dataframe description: \n%s' % observation_df.describe(include='all'))

    # Return observations DF
    return observation_df


def q1(df):
    # print df[['email_version', 'opened_flag', 'row_weight']].groupby(by=['email_version', 'opened_flag']).count()

    print df[['opened_flag', 'row_weight', 'CTA_link_click']].groupby(by=['opened_flag']).agg(
        {'row_weight': np.sum, 'CTA_link_click': np.sum})
    # print df['opened_flag'].value_counts()
    # print df[df['opened_flag']]['CTA_link_click'].value_counts()
    # print df[~df['opened_flag']]['CTA_link_click'].value_counts()


    print df[(df['opened_flag']) & (df['CTA_link_click'])].shape

    print df[(df['opened_flag']) & ~(df['CTA_link_click'])].shape
    print df[(~df['opened_flag']) & (df['CTA_link_click'])].shape
    print df[(~df['opened_flag']) & ~(df['CTA_link_click'])].shape


def q2(df):
    print df['CTA_link_click'].value_counts()
    y, X = patsy.dmatrices('CTA_link_click ~ user_past_purchases + user_country + np.sin(hour) + np.cos(hour)',
                           data=df, return_type='dataframe')

    print y
    print X
    mod = sm.Logit(y['CTA_link_click[True]'], X)
    res = mod.fit()

    print res.summary()


def main():
    """
    Main function documentation template
    :return: None
    :rtype: None
    """

    # Create dataset
    df = create_training_df()
    q1(df)
    q2(df)


# Main section
if __name__ == '__main__':
    main()
