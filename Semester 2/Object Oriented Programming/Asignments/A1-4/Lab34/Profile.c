#include "Profile.h"

Profile * createProfile(char * profileIdNumber, char * placeOfBirth, char * psychologicalProfile, int yearsOfRecordedService)
{
	Profile *profile = (Profile*)malloc(sizeof(Profile));
	profile->profileIdNumber = (char*)malloc(sizeof(char)*(strlen(profileIdNumber) + 1));
	strcpy(profile->profileIdNumber, profileIdNumber);
	profile->placeOfBirth = (char*)malloc(sizeof(char)*(strlen(placeOfBirth) + 1));
	strcpy(profile->placeOfBirth, placeOfBirth);
	profile->psychologicalProfile = (char*)malloc(sizeof(char)*(strlen(psychologicalProfile) + 1));
	strcpy(profile->psychologicalProfile, psychologicalProfile);
	profile->yearsOfRecordedService = yearsOfRecordedService;
	return profile;
}

char * getID(Profile * profile)
{
	return profile->profileIdNumber;
}

char * getPlaceOfBirth(Profile * profile)
{
	return profile->placeOfBirth;
}

char * getPsychologicalProfile(Profile * profile)
{
	return profile->psychologicalProfile;
}

int getYearsOfRecordedService(Profile * profile)
{
	return profile->yearsOfRecordedService;
}

void destroyProfile(Profile* profileToDestroy)
{
	if (profileToDestroy == NULL)
		return;
	free(profileToDestroy->profileIdNumber);
	free(profileToDestroy->placeOfBirth);
	free(profileToDestroy->psychologicalProfile);
	free(profileToDestroy);
	
}

void toString(Profile* printProfile, char stringToConcatenate[])
{
	char auxiliary[41];
	strcpy(auxiliary, printProfile->profileIdNumber);
	strcat(stringToConcatenate, auxiliary);
	strcat(stringToConcatenate, " ");
	strcat(stringToConcatenate, printProfile->placeOfBirth);
	strcat(stringToConcatenate, " ");
	strcat(stringToConcatenate, printProfile->psychologicalProfile);
	strcat(stringToConcatenate, " ");
	itoa(printProfile->yearsOfRecordedService, auxiliary, 10);
	strcat(stringToConcatenate, auxiliary);
	strcat(stringToConcatenate, "\n");
}

Profile * copyProfile(Profile * profileToCopy)
{
	Profile* copy = (Profile*)malloc(sizeof(Profile));
	copy->profileIdNumber = (char*)malloc(sizeof(char)*(strlen(profileToCopy->profileIdNumber) + 1));
	strcpy(copy->profileIdNumber, profileToCopy->profileIdNumber);
	copy->placeOfBirth = (char*)malloc(sizeof(char)*(strlen(profileToCopy->placeOfBirth) + 1));
	strcpy(copy->placeOfBirth, profileToCopy->placeOfBirth);
	copy->psychologicalProfile = (char*)malloc(sizeof(char)*(strlen(profileToCopy->psychologicalProfile) + 1));
	strcpy(copy->psychologicalProfile, profileToCopy->psychologicalProfile);
	copy->yearsOfRecordedService = profileToCopy->yearsOfRecordedService;

	return copy;
}
