#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "stafffunction.h"

// Tay Hong Yi
// TP068258


const char leaveapproverpassword[20] = "Jason123"; 
const char admin_password[20] = "Jasonlol"; 
void adminlogin(void);
void leaveapproverlogin(void);



void unbuild(){
    printf("It had not have any information yet!");
}

void SComputing(){
    int facultyoption;

    printf("Please select your department:\n");
    printf("1) Faculty of Computer Science\n2) Faculty of Information Technology\n3) Faculty of Software Engineering");
    scanf("\n\n%d:",&facultyoption);

    switch (facultyoption){
        case 1:
            facultycs();
            break;
        case 2:
            unbuild();
            break;
        case 3:
            unbuild();
            break;
        default:
            printf("Please type in the correct integer of 1 to 3 only!");
    }
}

void facultycs(){
    int useroption;
    printf("\nWho are you? Please choose your choice:");
    printf("\n1) Admin (leave management)\n2) staff (leave application)\n3) superior (leave approval)");
    scanf("\n%d",&useroption);

    switch (useroption){
        case 1:
            adminlogin();
            break;
        case 2:
            printf("Hi");
            registerNewStaff();
            break;
        case 3:
        	leaveapproverlogin();
	        break;
			
        default:
            printf("Please enter 1-3 only");}
    }


void adminlogin(){
	char adminpassword[20];
        printf("\n");
        printf("Please enter password to proceed:");
    	scanf("%s", adminpassword);

        if (strcmp(adminpassword, admin_password) != 0) {
            printf("Invalid password. Exiting...\n");
            
            return;}
        else{
        	adminoption();
        	return;
		}
}



void adminoption(){
	int useroption;
    printf("\nPlease choose your choice:");
    printf("\n1) Register\n2) Add the leave details after leave approver approved or reject someone's leave application\n3) Update the leave balance for the staff\n4) Search staff's leave information using staffID\n5) Open the monthly report for the leave statistics of faculty of computer science\n6) Modify the monthly report");
    scanf("\n%d",&useroption);

    switch (useroption){
        case 1:
            printf("You have choose to register a new staff...");
            registerNewStaff();
            break;
        case 2:
            printf("You had choose to add leave details for the staff..");
            addleavedetails();
            break;
        case 3:
			updateleave();
	        break;
		case 4:
			search_staff();
			break;
		case 5:
			openreport();
			break;
		case 6:
			modifyreport();
			break;
        default:
            printf("Please enter 1-6 only");
            break;
    }
}

void staffoption(){
	int staffchoice;
    printf("\nPlease choose your choice:");
    printf("\n1) Apply leave\n2) cancel leave\n3) Check leave status and information");
    scanf("\n%d",&staffchoice);

    switch (staffchoice){
        case 1:
            applyleave();
            break;
        case 2:
            cancelleave();
            break;
        case 3:
            check_leavestatus_or_leavebalance();
            break;
        default:
            printf("Please enter 1-3 only");
            break;
    }

}

void leaveapproverlogin(){
	char leaveapproverpasswords[20];
        printf("\n");
        printf("Please enter password:");
    	scanf("%s", leaveapproverpasswords);

        if (strcmp(leaveapproverpasswords, leaveapproverpassword) != 0) {
            printf("Invalid password. Exiting...\n");
            return;}
        else{
        	// function superior can do
        	leaveapproverfunction();
}}


void leaveapproverfunction(){
	int leaveapproveroption;

    printf("Please select your choice:\n");
    printf("1) Approve or reject leave application\n2) Search a date and view the number of staff who applied leave on the specified date\n");
    scanf("\n%d:",&leaveapproveroption);

    switch (leaveapproveroption){
        case 1:
			approve_or_reject_leave();
            break;
        case 2:
        	searchreport();
            break;
        default:
            printf("Please type in the correct integer of 1 to 2 only!");
    }
}





int main(){

    int option1;

    printf("------------Welcome to APU leave management system!------------\n");
    printf("            Please select your school:\n            1.	School of Computing and Technology\n            2.	School of Engineering\n            3.	School of Business and Management\n            4.	School of Accounting, Finance and Quantitative Studies\n            5.	School of Foundation Studies\n            6.	School of Postgraduate Studies\n------------7.	School of Media, Arts and Design------------\n");
    scanf("\n%d",&option1);

    switch (option1){
        case 1:
            SComputing();
            break;
        case 2:
            unbuild();
            break;
        case 3:
            unbuild();
            break;
        case 4:
            unbuild();
            break;
        case 5:
            unbuild();
            break;
        case 6:
            unbuild();
            break;
        case 7:
            unbuild();
            break;
        default:
            printf("Please type in the correct integer of 1 to 7 only!");
    	return 1;
    }

    return 0;
}

