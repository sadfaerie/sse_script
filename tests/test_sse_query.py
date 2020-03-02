import pytest
import sys, io
import mongomock

from sse_script import sse_query

events = [
    {"studentId":"Palma98","exam":5805,"score":0.8317752561891837},
    {"studentId":"Janie.Hettinger","exam":5805,"score":0.7633660664593065},
    {"studentId":"Wilber33","exam":5805,"score":0.6682357826838325}, 
    {"studentId":"Shyann43","exam":5805,"score":0.7096464894417537}
]

collection = mongomock.MongoClient().db.collection
collection.insert_many(events)
sse_query.collection = collection

def test_list_all_users():

    capturedOutput = io.StringIO()        
    sys.stdout = capturedOutput  

    sse_query.list_all_users()

    sys.stdout = sys.__stdout__
    assert "Palma98" in capturedOutput.getvalue()


def test_list_exam_results_for_student():

    capturedOutput = io.StringIO()        
    sys.stdout = capturedOutput  

    sse_query.list_exam_results_for_student("Palma98")

    sys.stdout = sys.__stdout__
    assert "5805" in capturedOutput.getvalue()


def test_list_all_exams():

    capturedOutput = io.StringIO()        
    sys.stdout = capturedOutput  

    sse_query.list_all_exams()

    sys.stdout = sys.__stdout__
    assert "5805" in capturedOutput.getvalue()


def test_list_all_results_for_exam():

    capturedOutput = io.StringIO()        
    sys.stdout = capturedOutput  

    sse_query.list_all_results_for_exam("5805")

    sys.stdout = sys.__stdout__
    assert "0.7096464894417537" in capturedOutput.getvalue()