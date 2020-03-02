#!/usr/bin/env python3

import pymongo
import termcolor, pyfiglet

from constants import *

mongo_client = pymongo.MongoClient(MONGO_HOST, 27017)
db = mongo_client.pymongo_sse
collection = db.events


def main():
    run_header()
    print_menu()

    while True:
        make_selection()

def run_header():
    header = pyfiglet.figlet_format("SseQuery")
    header = termcolor.colored(header, color="cyan")
    print(header)

def print_menu():
    print("\033[4mPress a key to select an option:\033[0m")
    print("\033[1m[1]\033[0m List all students")
    print("\033[1m[2]\033[0m List exam results for a student")
    print("\033[1m[3]\033[0m List all exams")
    print("\033[1m[4]\033[0m List all results for an exam")
    print("\033[1m[5]\033[0m Quit")
    
def make_selection():
    
    while True:
        selection = input("\n>> ")
        if selection == "1":
            list_all_users()
        elif selection == "2":
            list_exam_results_for_student()
        elif selection == "3":
            list_all_exams()
        elif selection == "4":
            list_all_results_for_exam()
        elif selection == "5" or selection == "q".lower():
            print("Goodbye!")
            exit()
        elif "12345" not in selection:
            print("\033[91mInvalid selection.\033[0m")
            print_menu()
            continue
        else:
            break


def list_all_users():
    """ An operation to list all the users that have received at least one exam score. """

    students = collection.distinct("studentId")
    print("\033[92mListing all users that have received at least one exam score:\033[0m")
    for student in students:
        print("-", student)

def list_exam_results_for_student(input_student=None):
    """ An operation to list all the exam results for a specified student ID. """

    if input_student == None:
        input_student = input("Provide the name of a student to look for:\n>> ")
    
    student_results = collection.find({"studentId":input_student})
    if input_student in student_results.distinct("studentId"):
        print("\n\033[92mListing all the exam results for \033[1m{}\033[0m:\033[0m".format(input_student))
        print("Exam : result")
        for result in student_results:
            print(result["exam"], ":", result["score"])
    else:
        print("\033[91mDid not find match for \"{}\".\033[0m".format(input_student))
        while True:
            select = input("Try \033[1m[A]\033[0mgain or go back to selection \033[1m[M]\033[0menu: ").lower()
            if "m" in select:
                return main()
            elif "a" in select:
                return list_exam_results_for_student()
            else:
                break

def list_all_exams():
    """ An operation to list all the exams that have been recorded. """

    print("\033[92mPrinting all exams that have been recorded:\033[0m")
    exams = collection.distinct("exam")
    print(exams)

def list_all_results_for_exam(input_exam=None):
    """ An operation to list all the results for a specified exam. """

    if input_exam == None:
        input_exam = input("Provide the number of the exam to look for:\n>> ")
    exam_results = collection.find({"exam":int(input_exam)})
    print("\033[92mPrinting results from exam \033[1m{}\033[0m:\033[0m".format(input_exam))
    for result in exam_results:
        print(result["score"])



if __name__ == "__main__":
    main()