class Converter:
    conversions= {
        'inches': 1,
        'feet': 12,
        'yards': 36,
        'miles': 63360,
        'kilometers': 39370.1,
        'meters': 39.3701,
        'centimeters': 0.393701,
        'millimeters': 0.0393701
    }

    def __init__(self, length, unit):
        if unit not in self.conversions:
            raise ValueError(f"Unsupported unit: {unit}")
        self.len_in_inches = length * self.conversions[unit]

    def inches(self):
        return self.len_in_inches

    def feet(self):
        return self.len_in_inches / self.conversions['feet']

    def yards(self):
        return self.len_in_inches / self.conversions['yards']

    def miles(self):
        return self.len_in_inches / self.conversions['miles']

    def kilometers(self):
        return self.len_in_inches / self.conversions['kilometers']
    def meters(self):
        return self.len_in_inches / self.conversions['meters']

    def centimeters(self):
        return self.len_in_inches / self.conversions['centimeters']

    def millimeters(self):
        return self.len_in_inches / self.conversions['millimeters']

n=int(input('Enter no of test cases: '))
for i in range(n):
    num=int(input('Enter the length(in inches): '))
    c=Converter(num,'inches')
    print(c.inches())
    print(c.feet())
    print(c.meters()) 

