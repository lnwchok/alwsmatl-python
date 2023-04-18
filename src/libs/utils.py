### Data Listing
def List_input_material():
    return {'a0a': 'A53B-SMLS', 'a1a': 'A53B-ERW', 'a0c': 'A106B', 'c0a': 'A312-TP304-SMLS', 'c1a': 'A312-TP304-EFW'}

### Allowance Stress
# Linear Interpolation
# y = y 1 + ( x − x 1 ) ( y 2 − y 1 ) / x 2 − x 1.
def LInterpolate(x: float, x1: float, x2: float, y1:float, y2:float) -> float:
    return y1 + (x - x1) * (y2-y1) / (x2 - x1)


# Convert temperature from Celcius to Farenheit
def convertC2F(C: float) -> float:
    return C*1.8 + 32

# Find Lower and Upper Limit for Input's Temperature
def findTempLimit(Tin: float):
    # Return [0,0] is Temperature is out of Limit
    if Tin > 1500 or Tin <= 0: return [0, 0]
    # Follow normal statement
    if Tin > 0 and Tin <= 100: return [100, 100]
    if Tin > 100 and Tin <= 600:
        return [int(Tin / 100)*100, (int(Tin / 100)+1)*100]
    if Tin > 600 and Tin <=1500:
        return [int(Tin / 50)*50, (int(Tin / 50)+1)*50]


# Find  Allowance Stress
def findAllowStress(matl_code: str, T: float) -> float:
    with open('src/matldata.json','r') as f:
        data = json.load(f)
    if matl_code.upper() not in data: return -1
            # return {"errorflag": True, "message":  "Material " + matl_code + " is not found"}
    [Tl, Tu] = findTempLimit(T)
    T_label = "T{}"
    if Tl == 0 and Tu == 0: return -1
    elif Tl == Tu: return float(data[matl_code.upper()][T_label.format(Tl)])
    else:
        Sl = float(data[matl_code.upper()][T_label.format(Tl)])
        Su = float(data[matl_code.upper()][T_label.format(Tu)])
        return LInterpolate(T, Tl, Tu, Sl, Su)