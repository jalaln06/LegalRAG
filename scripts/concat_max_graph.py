import pandas as pd


def process_files(base_path, start_index, end_index, output_path):
    all_dataframes = []
    for i in range(start_index, end_index + 1):
        file_path = f"{base_path}_graph_{i}.csv"

        df = pd.read_csv(file_path)
        df.drop_duplicates(subset=df.columns[0], inplace=True)
        all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_csv(output_path, index=False)
    return final_df


process_files('data/max_graph/results', 1, 32, 'data/max_graph_proc/processed_second_graph.csv')
