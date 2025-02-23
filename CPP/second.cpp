// 
// There is 1 error in this file
// 

#include <iostream>
#include <vector>
#include <string>

class Student {
private:
    std::string name;
    int age;
    float gpa;

public:
    Student(std::string n, int a, float g) : name(n), age(a), gpa(g) {}

    void display() const {
        std::cout << "Name: " << name << ", Age: " << age << ", GPA: " << gpa << std::endl;
    }
};

class StudentManager {
private:
    std::vector<Student> students;

public:
    void addStudent(std::string name, int age, float gpa) {
        students.push_back(Student(name, age, gpa));
    }

    void displayStudents() const {
        if (students.empty()) {
            std::cout << "No students found." << std::endl;
            return;
        }

        for (const Student& s : students) {
            s.display();
        }
    }
};

int main() {
    StudentManager manager;

    manager.addStudent("Alice", 20, 3.8);
    manager.addStudent("Bob", 22, 3.5);
    manager.addStudent("Charlie", 19, 3.9);

    std::cout << "Student List:" << std::endl;
    manager.showStudents();

    return 0;
}
