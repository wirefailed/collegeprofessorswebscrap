USC_professors_infos = [['Ali Abbas', 'Professor of Industrial and Systems Engineering and Public Policy', ['2004, Doctoral Degree, Management Science and Engineering, Stanford University', '2004, Doctoral Degree, Electrical Engineering, Stanford University', "2002, Master's Degree, Industrial Engineering, Stanford University", "1998, Master's Degree, Electrical Engineering, Stanford University"]]]

for professor_info in USC_professors_infos:
            professor_name = professor_info[0]
            professor_academic_title = professor_info[1]

            print(professor_name)
            print('--------------')
            print(professor_academic_title)

            for degree_info in professor_info[2]:
                print('-------------------')
                print(degree_info)
