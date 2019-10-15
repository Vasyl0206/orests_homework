class Ball(object):
    def __init__(self,ball_type = "regular"):
        self.ball_type = ball_type
    def ball_type(self):
        if self.ball_type == '':
           print ("regular")
        elif self.ball_type == 'super':
           print ("super")

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"