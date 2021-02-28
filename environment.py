class Environment:
    def set_size(self, x, y):
        self.size = [x,y]
        self.agents = []

    def get_size(self):
        return(self.size)
    
    def set_agents(self, agent):
        self.agents = self.agents + [agent,]
    
    def get_agents(self):
        return(self.agents)
    
    def clear_environment(self):
        self.agents = []