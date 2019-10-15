class Ball(object):
    def __init__(self,ball_type = None):
        self.ball_type = ball_type
        if self.ball_type is None:
           self.ball_type = 'regular'
        elif: 
           self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"
