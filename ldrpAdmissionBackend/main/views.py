from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import uuid
import json
from .models import formTable

def index(request):
    if request.method == "POST":
        ACPCRank = request.POST["ACPCRank"]
        DOB = request.POST["DOB"]
        GUJCETRollNo = request.POST["GUJCETRollNo"]
        POB = request.POST["POB"]
        bloodGroup = request.POST["bloodGroup"]
        board = request.POST["board"]
        category = request.POST["category"]
        city = request.POST["city"]
        city3 = request.POST["city3"]
        cityOfPermanentAddress = request.POST["cityOfPermanentAddress"]
        course = request.POST["course"]
        date = request.POST["date"]
        fatherName = request.POST["fatherName"]
        fatherName2 = request.POST["fatherName2"]
        gender = request.POST["gender"]
        grandFatherName = request.POST["grandFatherName"]
        gujcetYear = request.POST["gujcet-year"]
        gujcetBoard = request.POST["gujcet-board"]
        gujcetClass = request.POST["gujcet-class"]
        gujcetMark = request.POST["gujcet-mark"]
        gujcetPercentage = request.POST["gujcet-percentage"]
        gujcetPecentile = request.POST["gujcet-pecentile"]
        hscYear = request.POST["hsc-year"]
        hscBoard = request.POST["hsc-board"]
        hscClass = request.POST["hsc-class"]
        hscMark = request.POST["hsc-mark"]
        hscPercentage = request.POST["hsc-percentage"]
        hscPecentile = request.POST["hsc-pecentile"]
        hscAllYear = request.POST["hscAll-year"]
        hscAllBoard = request.POST["hscAll-board"]
        hscAllClass = request.POST["hscAll-class"]
        hscAllMark = request.POST["hscAll-mark"]
        hscAllPercentage = request.POST["hscAll-percentage"]
        hscAllPecentile = request.POST["hscAll-pecentile"]
        localAddress = request.POST["localAddress"]
        medium = request.POST["medium"]
        motherName = request.POST["motherName"]
        nameOfSchool = request.POST["nameOfSchool"]
        nameOfTheStudent = request.POST["nameOfTheStudent"]
        parentMobileNo = request.POST["parentMobileNo"]
        parentOccupation = request.POST["parentOccupation"]
        parentOccupationAddress = request.POST["parentOccupationAddress"]
        passportPhoto = request.POST["passportPhotoUrl"]
        permanentAddress = request.POST["permanentAddress"]
        pinCode = request.POST["pinCode"]
        pinCode3 = request.POST["pinCode3"]
        pinCodeOfPermanentAddress = request.POST["pinCodeOfPermanentAddress"]
        religion = request.POST["religion"]
        round = request.POST["round"]
        signOfParent = request.POST["signOfParentUrl"]
        signOfStudent = request.POST["signOfStudentUrl"]
        sscYear = request.POST["ssc-year"]
        sscBoard = request.POST["ssc-board"]
        sscClass = request.POST["ssc-class"]
        sscMark = request.POST["ssc-mark"]
        sscPercentage = request.POST["ssc-percentage"]
        sscPecentile = request.POST["ssc-pecentile"]
        studentEmail = request.POST["studentEmail"]
        studentMobileNo1 = request.POST["studentMobileNo1"]
        studentMobileNo2 = request.POST["studentMobileNo2"]
        studentName = request.POST["studentName"]
        surname = request.POST["surname"]
        surname2 = request.POST["surname2"]

        # check if session exists
        if request.session.has_key("studentEmail") and request.session.has_key("studentMobileNo1") and request.session.has_key("nameOfTheStudent"):
            oldEntry = formTable.objects.filter(studentEmail=request.session["studentEmail"], studentMobileNo1=request.session["studentMobileNo1"], nameOfTheStudent=request.session["nameOfTheStudent"],ACPCRank=request.session["ACPCRank"], GUJCETRollNo=request.session["GUJCETRollNo"]).first()
            oldEntry.ACPCRank = ACPCRank
            oldEntry.DOB = DOB.split("/")[2]+"-"+DOB.split("/")[1]+"-"+DOB.split("/")[0]
            oldEntry.GUJCETRollNo = GUJCETRollNo
            oldEntry.POB = POB
            oldEntry.bloodGroup = bloodGroup
            oldEntry.board = board
            oldEntry.category = category
            oldEntry.city = city
            oldEntry.city3 = city3
            oldEntry.cityOfPermanentAddress = cityOfPermanentAddress
            oldEntry.course = course
            oldEntry.date = date.split("/")[2]+"-"+date.split("/")[1]+"-"+date.split("/")[0]
            oldEntry.fatherName = fatherName
            oldEntry.fatherName2 = fatherName2
            oldEntry.gender = gender
            oldEntry.grandFatherName = grandFatherName
            oldEntry.gujcetBoard = gujcetBoard
            oldEntry.gujcetClass = gujcetClass
            oldEntry.gujcetMark = gujcetMark
            oldEntry.gujcetPecentile = gujcetPecentile
            oldEntry.gujcetPercentage = gujcetPercentage
            oldEntry.gujcetYear = gujcetYear
            oldEntry.hscBoard = hscBoard
            oldEntry.hscClass = hscClass
            oldEntry.hscMark = hscMark
            oldEntry.hscPecentile = hscPecentile
            oldEntry.hscPercentage = hscPercentage
            oldEntry.hscYear = hscYear
            oldEntry.hscAllBoard = hscAllBoard
            oldEntry.hscAllClass = hscAllClass
            oldEntry.hscAllMark = hscAllMark
            oldEntry.hscAllPecentile = hscAllPecentile
            oldEntry.hscAllPercentage = hscAllPercentage
            oldEntry.hscAllYear = hscAllYear
            oldEntry.localAddress = localAddress
            oldEntry.medium = medium
            oldEntry.motherName = motherName
            oldEntry.nameOfSchool = nameOfSchool
            oldEntry.nameOfTheStudent = nameOfTheStudent
            oldEntry.parentMobileNo = parentMobileNo
            oldEntry.parentOccupation = parentOccupation
            oldEntry.parentOccupationAddress = parentOccupationAddress
            oldEntry.passportPhoto = passportPhoto
            oldEntry.permanentAddress = permanentAddress
            oldEntry.pinCode = pinCode
            oldEntry.pinCode3 = pinCode3
            oldEntry.pinCodeOfPermanentAddress = pinCodeOfPermanentAddress
            oldEntry.religion = religion
            oldEntry.round = round
            oldEntry.signOfParent = signOfParent
            oldEntry.signOfStudent = signOfStudent
            oldEntry.sscBoard = sscBoard
            oldEntry.sscClass = sscClass
            oldEntry.sscMark = sscMark
            oldEntry.sscPecentile = sscPecentile
            oldEntry.sscPercentage = sscPercentage
            oldEntry.sscYear = sscYear
            oldEntry.studentEmail = studentEmail
            oldEntry.studentMobileNo1 = studentMobileNo1
            oldEntry.studentMobileNo2 = studentMobileNo2
            oldEntry.studentName = studentName
            oldEntry.surname = surname
            oldEntry.surname2 = surname2
            oldEntry.save()
        else:
            newEntry = formTable()
            newEntry.ACPCRank = ACPCRank
            newEntry.DOB = DOB.split("/")[2]+"-"+DOB.split("/")[1]+"-"+DOB.split("/")[0]
            newEntry.GUJCETRollNo = GUJCETRollNo
            newEntry.POB = POB
            newEntry.bloodGroup = bloodGroup
            newEntry.board = board
            newEntry.category = category
            newEntry.city = city
            newEntry.city3 = city3
            newEntry.cityOfPermanentAddress = cityOfPermanentAddress
            newEntry.course = course
            newEntry.date = date.split("/")[2]+"-"+date.split("/")[1]+"-"+date.split("/")[0]
            newEntry.fatherName = fatherName
            newEntry.fatherName2 = fatherName2
            newEntry.gender = gender
            newEntry.grandFatherName = grandFatherName
            newEntry.gujcetBoard = gujcetBoard
            newEntry.gujcetClass = gujcetClass
            newEntry.gujcetMark = gujcetMark
            newEntry.gujcetPecentile = gujcetPecentile
            newEntry.gujcetPercentage = gujcetPercentage
            newEntry.gujcetYear = gujcetYear
            newEntry.hscBoard = hscBoard
            newEntry.hscClass = hscClass
            newEntry.hscMark = hscMark
            newEntry.hscPecentile = hscPecentile
            newEntry.hscPercentage = hscPercentage
            newEntry.hscYear = hscYear
            newEntry.hscAllBoard = hscAllBoard
            newEntry.hscAllClass = hscAllClass
            newEntry.hscAllMark = hscAllMark
            newEntry.hscAllPecentile = hscAllPecentile
            newEntry.hscAllPercentage = hscAllPercentage
            newEntry.hscAllYear = hscAllYear
            newEntry.localAddress = localAddress
            newEntry.medium = medium
            newEntry.motherName = motherName
            newEntry.nameOfSchool = nameOfSchool
            newEntry.nameOfTheStudent = nameOfTheStudent
            newEntry.parentMobileNo = parentMobileNo
            newEntry.parentOccupation = parentOccupation
            newEntry.parentOccupationAddress = parentOccupationAddress
            newEntry.passportPhoto = passportPhoto
            newEntry.permanentAddress = permanentAddress
            newEntry.pinCode = pinCode
            newEntry.pinCode3 = pinCode3
            newEntry.pinCodeOfPermanentAddress = pinCodeOfPermanentAddress
            newEntry.religion = religion
            newEntry.round = round
            newEntry.signOfParent = signOfParent
            newEntry.signOfStudent = signOfStudent
            newEntry.sscBoard = sscBoard
            newEntry.sscClass = sscClass
            newEntry.sscMark = sscMark
            newEntry.sscPecentile = sscPecentile
            newEntry.sscPercentage = sscPercentage
            newEntry.sscYear = sscYear
            newEntry.studentEmail = studentEmail
            newEntry.studentMobileNo1 = studentMobileNo1
            newEntry.studentMobileNo2 = studentMobileNo2
            newEntry.studentName = studentName
            newEntry.surname = surname
            newEntry.surname2 = surname2
            newEntry.save()

        request.session["nameOfTheStudent"] = nameOfTheStudent
        request.session["studentEmail"] = studentEmail
        request.session["studentMobileNo1"] = studentMobileNo1
        request.session["ACPCRank"] = ACPCRank
        request.session["GUJCETRollNo"] = GUJCETRollNo
        
        return redirect("/page2/")
    return render(request, "index.html")

def page2(request):
    if request.method == "POST":
        ACPCRank= request.session["ACPCRank"]
        GUJCETRollNo = request.session["GUJCETRollNo"] 
        nameOfTheStudent = request.session["nameOfTheStudent"]
        studentEmail = request.session["studentEmail"]
        studentMobileNo1 = request.session["studentMobileNo1"]
        date = request.POST["date"]
        signOfStudent = request.POST["signOfStudentUrl"]
        signOfParent = request.POST["signOfParentUrl"]

        entry = formTable.objects.filter(studentEmail=studentEmail, studentMobileNo1=studentMobileNo1, nameOfTheStudent=nameOfTheStudent,ACPCRank=ACPCRank, GUJCETRollNo=GUJCETRollNo).first()
        entry.date = date.split("/")[2]+"-"+date.split("/")[1]+"-"+date.split("/")[0]
        entry.signOfStudent = signOfStudent
        entry.signOfParent = signOfParent
        entry.save()
        return redirect("/page3/")
    return render(request, "page2.html")

def page3(request):
    if request.method == "POST":
        ACPCRank= request.session["ACPCRank"]
        GUJCETRollNo = request.session["GUJCETRollNo"]
        studentEmail = request.session["studentEmail"]
        studentMobileNo1 = request.session["studentMobileNo1"]
        date = request.POST["date"]
        signOfStudent = request.POST["signOfStudentUrl"]
        signOfParent = request.POST["signOfParentUrl"]
        nameOfTheStudent = request.POST["nameOfTheStudent"]
        course = request.POST["course"]

        entry = formTable.objects.filter(studentEmail=studentEmail,studentMobileNo1=studentMobileNo1,ACPCRank=ACPCRank,GUJCETRollNo=GUJCETRollNo).first()
        entry.date = date.split("/")[2]+"-"+date.split("/")[1]+"-"+date.split("/")[0]
        entry.signOfStudent = signOfStudent
        entry.signOfParent = signOfParent
        entry.nameOfTheStudent = nameOfTheStudent
        entry.course = course
        entry.save()
        return redirect("/page4/")
    return render(request, "page3.html")

def page4(request):
    return render(request, "page4.html")

@csrf_exempt
def pdf(request):
    return render(request, "pdf.html")

@csrf_exempt
def imageUpload(request):
    if request.method == "POST":
        image = request.FILES["image"]
        imageName = str(uuid.uuid4())
        with open("media/images/" + imageName+".png", "wb") as f:
            for chunk in image.chunks():
                f.write(chunk)
        return HttpResponse(json.dumps({"image": imageName+".png"}), content_type="application/json")
    else:
        return HttpResponse("You are not allowed to access this page.")