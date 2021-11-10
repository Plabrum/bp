import os

class Model_dirs():
    def __init__(self, dir_name=None):
        if dir_name is None: dir_name = "stan_files"    
        self.cur_dir = os.getcwd()
        self.stan_dir = os.path.join(os.getcwd(), dir_name)
        try:
            os.mkdir(self.stan_dir)
        except:
            print("overwriting directory")
        self.stan_model = os.path.join(self.stan_dir, "stan_model.stan")
        
    def create_files(self, s_model):
        f = open(self.stan_model, "w")
        f.write(s_model)
        f.close()