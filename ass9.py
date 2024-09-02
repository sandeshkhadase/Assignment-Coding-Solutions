def evaluate(expression):
  new_exp = expression.replace("plus", "+")
  new_exp = new_exp.replace("minus", "-")
  new_exp = new_exp.replace("times", "*")
  new_exp = new_exp.replace("divided by", "/")
  res = float(eval(new_exp))
  return res
