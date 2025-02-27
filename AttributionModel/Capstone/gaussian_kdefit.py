import pandas as pd
import pickle
from scipy import stats
import luigi
import state_to_state_transitions2 as sst
class save_distributions(luigi.Task):
    file_tag = luigi.Parameter()
    source = luigi.Parameter()
    def run(self):
        path = 'C:\\Users\\User\\Documents\\GitHub\\Springboard-DSC\\AttributionModel\\Data\\ModelData\\'
        data = pd.read_csv(path+self.file_tag+'.csv')
        # data.columns = ['index', 'probability']
        kernel = stats.gaussian_kde(data['probability'])
        #we fit the distribution and save as a pickle
        pickle.dump(kernel,open('C:\\Users\\User\\Documents\\GitHub\\Springboard-DSC\\AttributionModel\\Data\\ModelData\\'+str(self.file_tag)+'probabs'+'.pck','wb'))
    def requires(self):
        files = ['Session.csv','lead.csv','opportunity.csv','complete.csv']
        return [sst.state_to_state(first_file=files[i-1],second_file=files[i],source=self.source) for i in range(1,len(files))]
    def output(self):
        return luigi.LocalTarget('C:\\Users\\User\\Documents\\GitHub\\Springboard-DSC\\AttributionModel\\Data\\ModelData\\'+str(self.file_tag)+'probabs'+'.pck')

