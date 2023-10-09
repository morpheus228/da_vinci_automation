from abc import abstractmethod
import pandas as pd
import numpy as np


class Generator:
    def __init__(self, csv_path: str):
        self.csv_path: str = csv_path
        self.data: pd.DataFrame = pd.read_csv(csv_path, sep=';')
        self.index: int = self.get_index()

        print(self.data.iloc[self.index, 1])
        
    @abstractmethod
    def next(self) -> str|None:
        try:
            return self.data.iloc[self.index, 0]
        except:
            return None

    def label(self, value: int):
        self.data.iloc[self.index, 1] = value
        self.index += 1
        self.save()

    def get_index(self) -> int:
        for index, row in self.data.iterrows():
            if np.isnan(row['Label']):
                return index
    
    def save(self):
        self.data.to_csv(self.csv_path, sep=';', index=False)

            
class ImagesGenerator(Generator):
    def __init__(self, csv_path: str):
        super().__init__(csv_path)

    def next(self) -> dict|None:
        path = super().next()
        if path is not None:
            return {'id': path}
        # 'path': f"data/images/{path}", 


ig = ImagesGenerator("data/images.csv")
# print(ig.next())




