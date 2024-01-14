user_groups = [
    "MENTOR",
    "STUDENT",
    "SUPER_ADMIN",
    "MACHINE",
]

departments = [
    {'name': 'Bcom-cs'},
    {'name': 'Bcom-acc'},
    {'name': 'Bsc-as'},
]

classes = [
    {'name': '1-a', 'batch': '2024', 'department': 'Bcom-cs'},
    {'name': '1-b', 'batch': '2024', 'department': 'Bcom-cs'},
    {'name': '2-a', 'batch': '2024', 'department': 'Bsc-as'},
]


mentors = [
    {'username': 'mentor1', 'email': 'mentor1@gmail.com',  'roll': '22MEN01'},
    {'username': 'mentor2', 'email': 'mentor2@gmail.com',  'roll': '22MEN02'},
    {'username': 'mentor3', 'email': 'mentor3@gmail.com',  'roll': '22MEN03'},
    {'username': 'mentor4', 'email': 'mentor4@gmail.com',  'roll': '22MEN04'},
]

subjects = [
    {'name': 'DSA', 'class': '1-a', 'handled_by': 'mentor4@gmail.com'},
    {'name': 'OOPS', 'class': '1-a', 'handled_by': 'mentor2@gmail.com'},
    {'name': 'BIG DATA', 'class': '1-b', 'handled_by': 'mentor2@gmail.com'},
    {'name': 'JAVA', 'class': '1-b', 'handled_by': 'mentor1@gmail.com'},
    {'name': 'PHYSICS', 'class': '2-a', 'handled_by': 'mentor3@gmail.com'},
]

students = [
    {'username': 'student1','email': 'student1@gmail.com',  'roll': '22KA01', 'batch': '2024', 'department': 'Bcom-cs', 'class': '1-a','mentor': 'mentor1@gmail.com'},
    {'username': 'student2','email': 'student2@gmail.com',  'roll': '22KA02' ,'batch': '2024', 'department': 'Bcom-cs', 'class': '1-a','mentor': 'mentor1@gmail.com'},
    {'username': 'student3', 'email': 'student3@gmail.com',  'roll': '22KA03', 'batch': '2024', 'department': 'Bcom-cs', 'class': '1-a','mentor': 'mentor1@gmail.com'},
    {'username': 'student4', 'email': 'student4@gmail.com',  'roll': '22KA04', 'batch': '2024', 'department': 'Bcom-cs', 'class': '1-a','mentor': 'mentor1@gmail.com'},
    {'username': 'student5', 'email': 'student5@gmail.com',  'roll': '22KA05', 'batch': '2024', 'department': 'Bcom-cs', 'class': '1-a','mentor': 'mentor1@gmail.com'},
    {'username': 'student6', 'email': 'student6@gmail.com',  'roll': '22KA06', 'batch': '2024', 'department': 'Bcom-cs', 'class': '1-b','mentor': 'mentor2@gmail.com'},
    {'username': 'student7', 'email': 'student7@gmail.com','roll': '22KA07', 'batch': '2024', 'department': 'Bcom-cs', 'class': '1-b','mentor': 'mentor2@gmail.com'},
    {'username': 'student8', 'email': 'student8@gmail.com', 'roll': '22KA08', 'batch': '2024', 'department': 'Bcom-cs', 'class': '1-b','mentor': 'mentor2@gmail.com'},
    {'username': 'student9', 'email': 'student9@gmail.com', 'roll': '22KA09', 'batch': '2024', 'department': 'Bcom-cs', 'class': '1-b','mentor': 'mentor2@gmail.com'},
    {'username': 'student10','email': 'student10@gmail.com', 'roll': '22KA10', 'batch': '2024', 'department': 'Bsc-as', 'class': '2-a','mentor': 'mentor3@gmail.com'}
]

