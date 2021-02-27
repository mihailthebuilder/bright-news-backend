import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def sen_stand(website_model_list, range_min, range_max):

    # reshape website list  so we can convert to pandas dataframe
    new_list = list(
        map(
            lambda website: {"url": website.url, "score": website.score},
            website_model_list,
        )
    )
    df = pd.DataFrame(new_list)

    # group rows by url by taking the mean
    grouped_df = df.groupby("url").mean()

    # scale all scores so they are between the two range values
    scaler = MinMaxScaler(feature_range=(range_min, range_max))
    grouped_df[["score"]] = scaler.fit_transform(grouped_df[["score"]])

    # sort values and reset structure to standard pandas dataframe
    reset_df = grouped_df.sort_values(by="score").reset_index()

    # convert dataframe to list
    website_li = list(reset_df.to_dict("index").values())
    return website_li