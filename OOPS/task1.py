# class Producer -- atributes  --- producer_name,production_comany  methods---producing print('producer_name is producing')

class Producer():

    def __init__(self,producer_name,production_company):

        self.producer_name = producer_name
        self.production_company = production_company



    def producing(self):
        print(f"{self.producer_name} is producing F1 at {self.production_company}")


producer_object = Producer("Jerry Bruckheimer and Lewis Hamilton", "Apple Studios")

producer_object.producing()