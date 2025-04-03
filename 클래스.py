class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result
calc = FourCal()
calc.setdata(10, 5)

print(calc.add())
print(calc.mul())
print(calc.div())

    
class Country:
    name = '국가명'
    population = '인구'
    capital = '수도'
    def show(self):
        print('국가 클래스의 메소드입니다.')
class Korea(Country):
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital
    def show_name(self):
        super().show() # 자식클래스 내에서 코드에서도 부모클래스를 호출출
        print("""국가 이름은 {} 입니다.
                 국가의 인구는 {} 입니다.
                 국가의 수도는 {} 입니다.
              """.format(self.name, self.population, self.capital))
a = Korea('대한민국', 50000000, '서울')
a.show()
a.show_name()
print(a.capital)
print(a.name)