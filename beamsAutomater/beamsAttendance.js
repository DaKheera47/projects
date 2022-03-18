function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}
var iframeDocument = document.getElementById("ii_core/mobile_app/sch_diary.php")
    .contentWindow.document;
var tbody = iframeDocument.getElementById("student_grid").children[1];

var data = [
    {
        studentName: "Naveera Seerat",
        id: "115831",
    },
    {
        studentName: "Yashfa Baloch",
        id: "141513",
    },
    {
        studentName: "Abroo Sajid Kiani",
        id: "161259",
    },
    {
        studentName: "Mannal Alizzah Hashmi",
        id: "3350000241872",
    },
    // {
    //     studentName: "Meher Ayub Khan",
    //     id: "169406",
    // },
    {
        studentName: "Maira Mustafa",
        id: "169406",
    },
    {
        studentName: "Manhal Fatima",
        id: "176650",
    },
    {
        studentName: "Amna Noor",
        id: "176652",
    },
    {
        studentName: "Eshaal Zeeshan",
        id: "178387",
    },
    {
        studentName: "Amna Noor",
        id: "183236",
    },
    {
        studentName: "Masjah Aziz",
        id: "204354",
    },
    {
        studentName: "Zahra Masud Khan",
        id: "221403",
    },
    {
        studentName: "Hamnah Afraz",
        id: "232408",
    },
    {
        studentName: "Aymen Shahzad",
        id: "235935",
    },
    {
        studentName: "Maria Faisal",
        id: "2320000212224",
    },
    {
        studentName: "Nayab Malik",
        id: "3230000246139",
    },
    {
        studentName: "Hiba Ishtiaq",
        id: "3260000246076",
    },
    {
        studentName: "Alyesha Asif Qureshi",
        id: "3320000242148",
    },
    {
        studentName: "Abeeha Fatima Mashhadi",
        id: "3350000247053",
    },
    {
        studentName: "Rumaisa Sajid",
        id: "6350000221983",
    },
    {
        studentName: "Ayesha Fatima",
        id: "6820000223025",
    },
    {
        studentName: "Umama Abbasi",
        id: "217078",
    },
];
// https://stackoverflow.com/questions/1129216/sort-array-of-objects-by-string-property-value
data.sort((a, b) =>
    a.studentName > b.studentName ? 1 : b.studentName > a.studentName ? -1 : 0
);
data.push({
    studentName: "Minal Kashif",
    id: "254059",
});
data.push({
    studentName: "Sameen Aftab",
    id: "210798",
});

var studentAttendance = [];

data.forEach((data) => {
    var choice = window.prompt(
        `Was ${data.studentName}: ${data.id} present [y/n] > `
    );

    // var attendance = [
    //     { studentName: "Naveera Seerat", status: "a", id: "115831" },
    //     { studentName: "Yashfa Baloch", status: "a", id: "141513" },
    //     { studentName: "Abroo Sajid Kiani", status: "a", id: "161259" },
    //     { studentName: "Maira Mustafa", status: "p", id: "169406" },
    //     { studentName: "Manhal Fatima", status: "p", id: "176650" },
    //     { studentName: "Amna Noor", status: "p", id: "176652" },
    //     { studentName: "Eshaal Zeeshan", status: "p", id: "178387" },
    //     { studentName: "Amna Noor", status: "a", id: "183236" },
    //     { studentName: "Masjah Aziz", status: "a", id: "204354" },
    //     { studentName: "Zahra Masud Khan", status: "a", id: "221403" },
    //     { studentName: "Hamnah Afraz", status: "p", id: "232408" },
    //     { studentName: "Aymen Shahzad", status: "p", id: "235935" },
    //     { studentName: "Maria Faisal", status: "p", id: "2320000212224" },
    //     { studentName: "Nayab Malik", status: "p", id: "3230000246139" },
    //     { studentName: "Hiba Ishtiaq", status: "a", id: "3260000246076" },
    //     { studentName: "Minal Kashif", status: "a", id: "254059" },
    //     { studentName: "Alyesha Asif Qureshi", status: "p", id: "3320000242148"},
    //     { studentName: "Abeeha Fatima Mashhadi", status: "p", id: "3350000247053"},
    //     { studentName: "Rumaisa Sajid", status: "p", id: "6350000221983" },
    //     { studentName: "Ayesha Fatima", status: "p", id: "6820000223025" },
    //     { studentName: "Sameen Aftab", status: "p", id: "210798" },
    //     { studentName: "Umama Abbasi", status: "a", id: "217078" },
    // ];

    // attendance.forEach((e) => {
    //     studentAttendance.push(e);
    // });
    // studentAttendance = attendance;

    choice === "y"
        ? studentAttendance.push({
              status: "p",
              studentName: data.studentName,
              id: data.id,
          })
        : studentAttendance.push({
              status: "a",
              studentName: data.studentName,
              id: data.id,
          });
});

var lenPresent = 0;
var lenAbsent = 0;
studentAttendance.forEach((student) => {
    student.status === "p" ? lenPresent++ : lenAbsent++;
});
console.log(`Number of students present: ${lenPresent}`);
console.log(`Number of students absent: ${lenAbsent}`);
console.log(studentAttendance);

for (var i = 0; i < tbody.children.length; i++) {
    // student name
    var studentNameFromDOM =
        tbody.children[i].children[1].children[0].textContent;

    // getting id
    // getting a tag of student name to get id from function call
    var el = tbody.children[i].children[1].children[0];
    var values = [];

    for (var att, f = 0, atts = el.attributes, n = atts.length; f < n; f++) {
        att = atts[f];
        values.push(att.nodeValue);
    }

    var studentIDFromDOM = values[1].split(",")[3].replace(")", "");
    var presentInPersonBtn = tbody.children[i].children[2].children[0];
    var presentOnlineBtn = tbody.children[i].children[2].children[1];
    var absentButton = tbody.children[i].children[2].children[3];
    // presentInPersonBtn.click();

    studentAttendance.forEach(async (data) => {
        if (studentIDFromDOM == data.id) {
            if (data.status === "a") {
                await sleep(2000);
                absentButton.click();
                await sleep(2000);
                // getting rid of the modal that shows
                var buttons = iframeDocument.getElementsByTagName("button");
                var searchText = "Ignore";
                var found;
                for (var p = 0; p < buttons.length; p++) {
                    if (buttons[p].textContent === searchText) {
                        found = buttons[p];
                        found.click();
                    }
                }
            } else if (data.status === "p") {
                await sleep(2000);
                presentInPersonBtn.click();
                await sleep(2000);
            }
        }
    });
}
