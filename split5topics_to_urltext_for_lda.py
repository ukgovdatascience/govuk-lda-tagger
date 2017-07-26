import csv
import pandas as pd
import re #regular expression
import click
import argparse

"""
This module/script takes the tagged url output from train_LDA with 5 topics, splits it into 5 groups and merges each group with original data to produce separate url, text.csvs ready to run LDA on

Example usage:
python create_bigrams.py input/test_urltext.csv input/test_bigrams.csv
"""  
__author__ = "Ellie King"
__copyright__ = "Government Digital Service, 10/07/2017"

parser = argparse.ArgumentParser(description=__doc__)

parser.add_argument(
    '--preLDA_fpath', dest='prelda_filename', metavar='FILENAME', default=None,
    help='import original url text data in csv'
)

parser.add_argument(
    '--tagged_fpath', dest='taggedurls_filename', metavar='FILENAME', default=None,
    help='import tagged urls in csv output from top level of hierarchy, first LDA'
)


def read_data(preLDA_fpath, tagged_fpath):
    """Function to read in original data and tagged documents after LDA with 5 topics"""
    df_tag5 = pd.read_csv(tagged_fpath, header=None, names=list('abcdefgh'))
    df_preLDA = pd.read_csv(preLDA_fpath)
    return(df_tag5, df_preLDA)

def clean_tagged_urls(df_tag5):
    """function to clean the dataframe to result in url 
    topic_id cols"""
    #drop the leading parentheses
    df_tag5['b'] = df_tag5['b'].str.replace(r'\[\(', '') 
    # drop the columns containing topics of lower (or equal probability)
    df2_tag5 =  df_tag5.drop(df_tag5.columns[[2, 3, 4, 5, 6, 7]], axis=1)
    # name the remaining two columns
    df2_tag5.columns = ['url', 'topic_id']
    return(df2_tag5)

def split_urls_by_topic(df_tag5_clean):
    #split dataframe into 5 separate dfs filtered on topic_id
    df_first_topic = df_tag5_clean.loc[df_tag5_clean['topic_id'] == '0']
    df_second_topic = df_tag5_clean.loc[df_tag5_clean['topic_id'] == '1']
    df_third_topic = df_tag5_clean.loc[df_tag5_clean['topic_id'] == '2']
    df_fourth_topic = df_tag5_clean.loc[df_tag5_clean['topic_id'] == '3']
    df_fifth_topic = df_tag5_clean.loc[df_tag5_clean['topic_id'] == '4']
    return(df_first_topic, df_second_topic, df_third_topic,  df_fourth_topic, df_fifth_topic)
    
def get_text_by_merging(df_first_topic, df_second_topic, df_third_topic,  df_fourth_topic, df_fifth_topic, df_preLDA):
    #merge on the index column to get text back from original url, text data
    df_first = pd.merge(df_first_topic, df_preLDA, left_index = True, right_index = True , indicator = True)
    df_second = pd.merge(df_second_topic, df_preLDA, left_index = True, right_index = True , indicator = True)
    df_third = pd.merge(df_third_topic, df_preLDA, left_index = True, right_index = True , indicator = True)
    df_fourth = pd.merge(df_fourth_topic, df_preLDA, left_index = True, right_index = True , indicator = True)
    df_fifth = pd.merge(df_fifth_topic, df_preLDA, left_index = True, right_index = True , indicator = True)
    return(df_first, df_second, df_third,  df_fourth, df_fifth)

def tidy_to_urltext(df_first, df_second, df_third, df_fourth, df_fifth):

    #keep only the url and text columns of the documents tagged with each topic
    df_first_tidy =  df_first.drop(df_first.columns[[1, 2, 4]], axis=1)
    df_second_tidy =  df_second.drop(df_second.columns[[1, 2, 4]], axis=1)
    df_third_tidy =  df_third.drop(df_third.columns[[1, 2, 4]], axis=1)
    df_fourth_tidy =  df_fourth.drop(df_fourth.columns[[1, 2, 4]], axis=1)
    df_fifth_tidy =  df_fifth.drop(df_fifth.columns[[1, 2, 4]], axis=1)

    #rename columns as they will be expected in train_LDA.py
    df_first_tidy.columns = ['url', 'text']
    df_second_tidy.columns = ['url', 'text']
    df_third_tidy.columns = ['url', 'text']
    df_fourth_tidy.columns = ['url', 'text']
    df_fifth_tidy.columns = ['url', 'text']
    return(df_first_tidy, df_second_tidy, df_third_tidy,  df_fourth_tidy, df_fifth_tidy)

def write_to_5_csvs(df_first, df_second, df_third,  df_fourth, df_fifth):
    df_first.to_csv(
        'enviro_experiments/DATA_environment_2017/dendro/first_top_PM.csv', index = False
        )
    df_second.to_csv(
        'enviro_experiments/DATA_environment_2017/dendro/second_top_PM.csv', index = False
        )
    df_third.to_csv(
        'enviro_experiments/DATA_environment_2017/dendro/third_top_PM.csv', index = False
        )
    df_fourth.to_csv(
        'enviro_experiments/DATA_environment_2017/dendro/fourth_top_PM.csv', index = False)
    df_fifth.to_csv(
        'enviro_experiments/DATA_environment_2017/dendro/fifth_top_PM.csv', index = False)

    return(df_tag5, df_preLDA)

if __name__ == '__main__':
    args = parser.parse_args()

    print("Loading input file {}".format(args.prelda_filename))
    print("Loading input file {}".format(args.taggedurls_filename))
    df_tag5, df_preLDA = read_data(
        preLDA_fpath = args.prelda_filename, 
        tagged_fpath = args.taggedurls_filename,
        )

    print(df_preLDA.head(10))

    print("Cleaning tags")
    df_tag5_clean = clean_tagged_urls(df_tag5)

    print("Splitting by topic")
    df_first_topic, df_second_topic, df_third_topic,  df_fourth_topic, df_fifth_topic = split_urls_by_topic(df_tag5_clean)

    print("Merging to text file")
    df_first, df_second, df_third,  df_fourth, df_fifth = get_text_by_merging(df_first_topic, 
        df_second_topic, 
        df_third_topic,  
        df_fourth_topic, 
        df_fifth_topic, 
        df_preLDA
        )

    print(df_fifth.head(10))

    print("Tidying up")
    df_first_tidy, df_second_tidy, df_third_tidy, df_fourth_tidy, df_fifth_tidy = tidy_to_urltext(
        df_first, 
        df_second, 
        df_third, 
        df_fourth, 
        df_fifth
        )

    print("Write to file")
    write_to_5_csvs(
        df_first_tidy, 
        df_second_tidy, 
        df_third_tidy,  
        df_fourth_tidy, 
        df_fifth_tidy
        )




#untested loop to rpelace lines above
#for topic_id in range(0, 5):
 #   df_topic_+str(topic_id + 1) = df2_tag5.loc[df2_tag5['topic_id'] == str(topic_id)#haven't tested this loop to replace the 5 lines below

