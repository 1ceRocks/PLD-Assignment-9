import json

personalDetails = {
  "primaryElements": [
    {
      "Full Name": "Fritz Cedrick V. Villariza",
      "Sex / Gender": "Male (M)",
      "Age": "18 Years Old",
      "Home Address": "554 Woodstock Drive, Beverly Hills, California City (CA), United States",
      "Height": "6'5",
      "Weight": "78"
    }
  ],
  "contactInformation": [
    {
      "Electronic Mail": "fcv1995@yahoo.com",
      "Smartphone Number (US +1, BH +30)": "929-345-6789",
      "Landline Number (BH +424)": "123-4567"
    }
  ],
  "academicBackground": [
    {
      "Elementary (1st to 6th Grade)": "City Tree Christian School",
      "Middle School (1st to 4th Year)": "Lashon Academy TK",
      "Senior High School (11th to 12th Grade)": "Los Angeles High School",
      "College (RECENT)": "Harvard University"
    }
  ],
  "elementaryAchievement/s": [
    "Best in Writing",
    "Most Obedient Award of the Year",
    "Most Behaved Student of the Class",
    "Christmas Jingle Champion"
  ],
  "middleSchoolAchievement/s": [
    "Best in Math (1st to 4th Year)",
    "Best in Science (2nd and 3rd Year)",
    "Best in History (4th Year)"
  ],
  "serniorHighAchievement/s": [
    "Rubiks' Cube 3rd Place Local Winner",
    "With High Honors (12th Grade)",
    "Song Writing Competition 4th Place",
    "Battle of the Bands Local Participant"
  ],
  "identityReference": [
    "Reyna Drip T. Cower",
    "Queen of England",
    "Oxford University",
    "0912-345-6789, +44 (0)1865 611530",
    "reyna12.driptcwr@devoff.ox.ac.uk"
  ],
  "personalExperience": [
    {
      "Microsoft Office": "Intermediate Capability",
      "Organizing System Unit": "Proficient Skill",
      "Music": "Rhythmic Guitarist",
      "E-Sports": "Platinum 3 - VALORANT"
    }
  ]
}

json_obj = json.dumps(personalDetails, indent = 2)
with open("personalDetails.json", "w") as collect:
  collect.write(json_obj)