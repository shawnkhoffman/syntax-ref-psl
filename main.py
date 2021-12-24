import funcs
import datatypes_strings
import datatypes_lists
import datatypes_tuples
import datatypes_iterations
import operators_division
import operators_assignment
import operators_identity
import operators_membership
import operators_ternary
import operator_overloading
import operators_any_all
import operator_functions


while True:
    funcs.clear_screen()
    funcs.about_program()

    main_topics = {
        '1': 'Data Types',
        '2': 'Operators',
        }
    main_topic_1 = main_topics['1']
    main_topic_2 = main_topics['2']

    datatypes_topics = {
        '1': 'Strings',
        '2': 'Lists',
        '3': 'Tuples',
        '6': 'Iterations'
    }
    datatypes_topic_1 = datatypes_topics['1']
    datatypes_topic_2 = datatypes_topics['2']
    datatypes_topic_3 = datatypes_topics['3']
    datatypes_topic_6 = datatypes_topics['6']

    strings_topics = {
        '1': 'Accessing Characters',
        '2': 'String Slicing',
        '3': 'Deleting/Updating from a String'
    }
    string_topic_1 = strings_topics['1']
    string_topic_2 = strings_topics['2']
    string_topic_3 = strings_topics['3']

    operator_topics = {
        '1': 'Assignment Operators',
        '2': 'Identity Operators',
        '3': 'Membership Operators',
        '4': 'Ternary Operators',
        '5': 'Division Operators',
        '6': 'Operator Overloading',
        '7': 'Any/All Operators',
        '8': 'Operator Functions'
    }
    operator_topic_1 = operator_topics['1']
    operator_topic_2 = operator_topics['2']
    operator_topic_3 = operator_topics['3']
    operator_topic_4 = operator_topics['4']
    operator_topic_5 = operator_topics['5']
    operator_topic_6 = operator_topics['6']
    operator_topic_7 = operator_topics['7']
    operator_topic_8 = operator_topics['8']

    while True:
        selected_topic = funcs.topic_selection(main_topics)

        try:
            if selected_topic is None:
                raise ValueError
        except ValueError:
            funcs.invalid_selection()
            continue
        else:
            break

    if selected_topic == main_topic_1:
        while True:
            funcs.clear_screen()
            funcs.your_selected_topic_is(selected_topic)
            selected_topic = funcs.topic_selection(datatypes_topics)

            try:
                if selected_topic is None:
                    raise ValueError
            except ValueError:
                funcs.invalid_selection()
                selected_topic = main_topic_1
                continue
            else:
                if selected_topic == 'back':
                    break
                while True:
                    if selected_topic == datatypes_topic_1:
                        while True:
                            selected_sub_topic = None
                            while True:
                                funcs.clear_screen()
                                datatypes_strings.intro()
                                selected_sub_topic = funcs.topic_selection(
                                    strings_topics
                                    )

                                try:
                                    if selected_sub_topic is None:
                                        raise ValueError
                                except ValueError:
                                    funcs.invalid_selection()
                                else:
                                    break

                            if selected_sub_topic == string_topic_1:
                                funcs.clear_screen()
                                datatypes_strings.accessing_chars()
                                answer = False
                                while answer is not True:
                                    answer = funcs.goback()

                            if selected_sub_topic == string_topic_2:
                                funcs.clear_screen()
                                datatypes_strings.string_slicing()
                                answer = False
                                while answer is not True:
                                    answer = funcs.goback()

                            if selected_sub_topic == string_topic_3:
                                funcs.clear_screen()
                                datatypes_strings.deleting_updating_string()
                                answer = False
                                while answer is not True:
                                    answer = funcs.goback()

                            elif selected_sub_topic == 'back':
                                selected_topic = main_topic_1
                                break

                    if selected_topic == datatypes_topic_2:
                        selected_sub_topic = None
                        funcs.clear_screen()
                        datatypes_lists.intro()
                        answer = False
                        while answer is not True:
                            answer = funcs.goback()

                    if selected_topic == datatypes_topic_3:
                        datatypes_tuples.intro()
                        while answer is not True:
                            answer = funcs.goback()

                    if selected_topic == datatypes_topic_6:
                        datatypes_iterations.intro()
                        while answer is not True:
                            answer = funcs.goback()

                    if answer is True:
                        selected_topic = main_topic_1
                        break

    if selected_topic == main_topic_2:
        while True:
            funcs.clear_screen()
            funcs.your_selected_topic_is(selected_topic)
            selected_topic = funcs.topic_selection(operator_topics)

            try:
                if selected_topic is None:
                    raise ValueError
            except ValueError:
                funcs.invalid_selection()
                selected_topic = main_topic_2
                continue
            else:
                if selected_topic == 'back':
                    break
                while True:
                    if selected_topic == operator_topic_1:
                        funcs.clear_screen()
                        operators_assignment.intro()
                        answer = False
                        while answer is not True:
                            answer = funcs.goback()

                        if answer is True:
                            selected_topic = main_topic_2
                            break

                    if selected_topic == operator_topic_1:
                        funcs.clear_screen()
                        operators_identity.intro()
                        answer = False
                        while answer is not True:
                            answer = funcs.goback()

                        if answer is True:
                            selected_topic = main_topic_2
                            break

                    if selected_topic == 'Membership Operators':
                        funcs.clear_screen()
                        operators_membership.intro()
                        answer = False
                        while answer is not True:
                            answer = funcs.goback()

                        if answer is True:
                            selected_topic = main_topic_2
                            break

                    if selected_topic == 'Ternary Operators':
                        funcs.clear_screen()
                        operators_ternary.intro()
                        answer = False
                        while answer is not True:
                            answer = funcs.goback()

                        if answer is True:
                            selected_topic = main_topic_2
                            break

                    if selected_topic == 'Division Operators':
                        funcs.clear_screen()
                        operators_division.intro()
                        answer = False
                        while answer is not True:
                            answer = funcs.goback()

                        if answer is True:
                            selected_topic = main_topic_2
                            break

                    if selected_topic == 'Operator Overloading':
                        funcs.clear_screen()
                        operator_overloading.intro()
                        answer = False
                        while answer is not True:
                            answer = funcs.goback()

                        if answer is True:
                            selected_topic = main_topic_2
                            break

                    if selected_topic == 'Any/All Operators':
                        funcs.clear_screen()
                        operators_any_all.intro()
                        answer = False
                        while answer is not True:
                            answer = funcs.goback()

                        if answer is True:
                            selected_topic = main_topic_2
                            break

                    if selected_topic == 'Operator Functions':
                        funcs.clear_screen()
                        operator_functions.intro()
                        answer = False
                        while answer is not True:
                            answer = funcs.goback()

                        if answer is True:
                            selected_topic = main_topic_2
                            break
