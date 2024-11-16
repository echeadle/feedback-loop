from crewai.flow.flow import Flow, listen, start

class ExampleFlow(Flow):
    
   @start()
   def generate_city(self):
      # TODO Generate a city
      return "New York"
   
   @listen(generate_city)
   def generate_fun_fact(self, random_city: str):
      # TODO Generate a fun fact about the city
      pass
     