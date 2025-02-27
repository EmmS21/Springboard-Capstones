import luigi
import pandas as pd
import state_to_state_transitions as ss
class state_to_state(luigi.Task):
    first_file = luigi.Parameter()
    second_file = luigi.Parameter()
    source = luigi.Parameter()
    def run(self):
        #iterate through states and find probability of anonymous id existing in next state
        path = "C:\\Users\\User\\Documents\\GitHub\\Springboard-DSC\\AttributionModel\\Data\ModelData\\"
        first = pd.read_csv(path+self.first_file)
        second = pd.read_csv(path+self.second_file)
        first['probability'] = first.anonymous_id.isin(second.anonymous_id).astype(int)
        #save anonymous id along with probability (1,0) of whether or not it exists in the next state
        first[['anonymous_id','probability']].to_csv('C:\\Users\\User\\Documents\\GitHub\\Springboard-DSC\\AttributionModel\\Data\\ModelData\\'+str(self.first_file[:-4]+'to'+self.second_file))
    def requires(self):
        # files_two = [sep.data_filter(file='/Users/emmanuels/Desktop/Attribution/finalcleanattributiondata.csv')]
        # yield files_two
        return [ss.ad_probabilities(file='Session.csv',source=self.source)]
    def output(self):
        return luigi.LocalTarget('C:\\Users\\User\\Documents\\GitHub\\Springboard-DSC\\AttributionModel\\Data\\ModelData\\'+str(self.first_file[:-4]+'to'+self.second_file))

