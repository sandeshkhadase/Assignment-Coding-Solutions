def highest_salary_per_employee(employees_salaries):
  
  for name, salary in employees_salaries.items():
    employees_salaries[name] = max(employees_salaries[name])
    
  return employees_salaries
  