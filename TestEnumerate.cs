using System;
using System.Collections;
using System.Collections.Generic;

namespace ConsoleApp2
{
    public class Employees
        : IEnumerable, IEnumerator
    {
        ArrayList _empList = new ArrayList();
        int _position = -1;
        public object Current => _empList[_position];
        public void AddEmployee(Employee oEmp)
        {
            _empList.Add(oEmp);
        }
        public IEnumerator GetEnumerator()
        {
            return (IEnumerator)this;
        }
        public bool MoveNext()
        {
            if (_position < _empList.Count - 1)
            {
                ++_position;
                return true;
            }
            else
            {
                return false;
            }
        }
        public void Reset()
        {
            _position = -1;
        }
    }
    class TestEnumerate
    {
        static void Main()
        {
            Employees frmltxEmployeeObj = new Employees();
            // Register new employee
            Employee employeeObj1 = new Employee("Bima", 26, 180);
            Employee employeeObj2 = new Employee("Jati", 25, 170);
            Employee employeeObj3 = new Employee("Wijaya", 24, 160);
            frmltxEmployeeObj.AddEmployee(employeeObj1);
            frmltxEmployeeObj.AddEmployee(employeeObj2);
            frmltxEmployeeObj.AddEmployee(employeeObj3);
            Console.WriteLine("\nEnumerating Employee Creating object of IEnumerator:");
            IEnumerator EmpEnumerator = frmltxEmployeeObj.GetEnumerator();
            EmpEnumerator.Reset();
            while (EmpEnumerator.MoveNext())
            {
                Employee employeeObj = (Employee)EmpEnumerator.Current;
                employeeObj.PrintInfo();
            }
            Console.WriteLine("\n===========\nCollection iterators:");
            List<Employee> employeeList = new List<Employee>
            {
                new Employee("Bima", 26, 180),
                new Employee("Jati", 27, 190),
                new Employee("Wijaya", 28, 200)
            };
            // or use employeeList.Add(new Emp...);
            foreach (Employee o in employeeList)
            {
                o.PrintInfo();
            }
            Console.ReadLine();
        }
    }
}
