import os
from pandas import DataFrame


def save_local(stock_df: DataFrame, directory: str, filename: str):
    """Save a Pandas DataFrame to multiple file formats in a specified directory."""

    # Create the directory if it does not exist
    if not os.path.exists(directory):
        os.mkdir(directory)

    # Create a file path template with placeholders for file extensions.
    path = os.path.join(directory, f"{filename}.%s")

    # save as excel
    stock_df.to_excel(path % "xlsx", index=False, sheet_name="stock")

    # save as csv
    stock_df.to_csv(path % "csv", index=False)

    # save as json
    stock_df.to_json(path % "json", orient="records")

    # save as pickle
    stock_df.to_pickle(path % "pkl")

    # save as xml
    stock_df.columns = [
        f"_{col}" if col[0].isdigit() else col for col in stock_df.columns
    ]
    stock_df.to_xml(path % "xml", index=False)
