class test:
    a=3
    def aaa(self):

        try:
            print('12333')
            if self.a != 0 :
                Print('666')


            # print('12345666')

        except Exception as e :
            if self.a == 0:
                raise  e
            self.a -= 1
            print('zhengshiyigeyichang')
            if self.a > 0:
                print('111')
            return self.aaa()



test().aaa()