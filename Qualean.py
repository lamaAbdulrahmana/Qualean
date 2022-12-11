import random

class qualean(object):
    
    def __init__(self,real_num):
        self._real_num = real_num
        self._img_num =  random.uniform(-1, 1)
        self._qualean_num = self.magic_number()
        
    def magic_number(self):
        return round(self._real_num * self._img_num , 10)
    
    #getters
    
    def get_real_num(self):
        return self._real_num
    def get_img_num(self):
        return self._img_num
    def get_qualean_num(self):
        return self._qualean_num
    
    #setters 
    
    def set_real_num(self,new_value):
        self._real_num = new_value
    def set_img_num(self,new_value):
        self._img_num = new_value
    def set_qualean_num(self,new_value):
        self._qualean_num = new_value
    
        
    def __add__(self, value):
        if isinstance (value, qualean):
            return qualean(self._qualean_num + value._qualean_num)
        return self._qualean_num + value
        
    def __sub__(self, value):
        if isinstance (value, qualean):
            return qualean(self._qualean_num - value._qualean_num)
        return self._qualean_num - value
           
    def __mul__(self, value):
        if isinstance (value, qualean):
            return qualean(self._qualean_num * value._qualean_num)
        return self._qualean_num * value    
    
    def __truediv__(self, value):
       if isinstance (value, qualean):
           return qualean(self._qualean_num / value._qualean_num)
       return self._qualean_num / value        
    
    def __and__(self, value):
        if isinstance (value, qualean):
            if value._qualean_num == 0 and value._qualean_num == 0:
                return False
            else:
                return True
        return False
    
    def __or__(self,value):
        if isinstance (value, qualean):
            if value._qualean_num == 0 or value._qualean_num == 0:
                return False
            else:
                return True   
        return False 
    
    def bool(self):
        if self._qualean_num == 0:
            return 0
        return 1
    
    def __eq__(self,value):
        if isinstance (value, qualean):
            return self._qualean_num == value._qualean_num
        return self._qualean_num == value
    
    def __float__(self):
        return float(self._qualean_num)
    
    def __ge__(self,value):
        if isinstance (value, qualean):
            return self._qualean_num >= value._qualean_num
        return self._qualean_num >= value
    
    def __invert__(self):
        self.set_qualean_num((-1) * self._qualean_num)
        self.magic_number()
      
    def __le__(self,value):
        if isinstance (value, qualean):
            return self._qualean_num <= value._qualean_num
        return self._qualean_num <= value
    
    def __lt__(self,value):
        if isinstance (value, qualean):
            return self._qualean_num < value._qualean_num
        return self._qualean_num < value
    
    
    def __gt__(self,value):
        if isinstance (value, qualean):
            return self._qualean_num > value._qualean_num
        return self._qualean_num > value
    
    def __sqrt__(self):
        return self._qualean_num ** 2
    
    def __str__(self):
        return 'The qualean number is %s' % self._qualean_num
    def __repr__(self):
        return 'The qualean number is %s' % self._qualean_num
        
q = qualean(1)
print(q.__repr__())