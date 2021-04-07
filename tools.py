from datetime import datetime as time


def timeit(func):
    def wrapper(a, b):
        start = time.now()
        found = func(a, b)
        print(func.__name__, ' => ', time.now() - start)
        return found

    return wrapper


# ex 1
@timeit
def linear_search(arr, element):
    for j in range(len(arr)):
        if arr[j] == element:
            return j
    return -1


# def binary_search_rec(arr, low, high, element):
#     if high >= low:
#         mid = (high + low) // 2
#         return mid if arr[mid] == element \
#             else binary_search_rec(arr, low, mid - 1, element) \
#             if arr[mid] > element \
#             else binary_search_rec(arr, mid + 1, high, element)
#
#     return -1


@timeit
def binary_search(arr, num):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            return mid

    return -1


# ex 2
@timeit
def direct_search(s, x):
    i = j = 0
    length_s = len(s)
    length_x = len(x)
    while i <= length_s - length_x and j < length_x:
        if s[i + j] == x[j]:
            j += 1
        else:
            i += 1
            j = 0
    return i if j == length_x else None


def predkompil(x):
    d = {0: 0}
    for i in range(1, len(x)):
        j = d[i - 1]
        while j > 0 and x[j] < x[i]:
            j = d[j - 1]
        if x[j] == x[i]:
            j += 1
        d[i] = j
    return d


@timeit
def kmp_search(s, x):
    d = predkompil(x)
    i = j = 0
    while i < len(s) and j < len(x):
        if x[j] == s[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = d[j - 1]
    else:
        if j == len(x):
            return i - j
        return None


# ex 3
NO_OF_CHARS = 256


def bad_char_heuristic(string, size):
    bad_char = [-1] * NO_OF_CHARS
    for i in range(size):
        bad_char[ord(string[i])] = i
    return bad_char


@timeit
def bm_search(main_str, sub_str):
    len_main = len(main_str)
    len_sub = len(sub_str)
    bad_char = bad_char_heuristic(sub_str, len_sub)
    i = 0
    while i <= len_main - len_sub:
        j = len_sub - 1
        while j >= 0 and sub_str[j] == main_str[i + j]:
            j -= 1
        if j < 0:
            print(f"BM: {i}")
            i += len_sub - bad_char[ord(main_str[i + len_sub])] if i + len_sub < len_main else 1
        else:
            i += max(1, j - bad_char[ord(main_str[i + j])])


main_string = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Perspiciatis accusamus sit quod velit fugit ipsam facilis! Quisquam, laborum asperiores rerum perferendis odit aspernatur expedita veniam quidem officia, ipsa facilis molestiae aliquid, pariatur aperiam natus! Illum nulla, aut suscipit provident perspiciatis culpa quod vel exercitationem doloribus explicabo amet magni rerum ab dAFDBolor obcaecati magnam, voluptatibus possimus cum consequuntur, nostrum facere quaerat incidunt. Porro placeat aperiam animi ex perspiciatis adipisci amet! Labore hic numquam, dolores eveniet repudiandae voluptate eum nostrum ex corrupti eaque! Incidunt labore eos debitis reAFDBAFDBAFDBcusandae! Mollitia tempore nobis eum illo explicabo hic excepturi culpa saepe ad in! Animi perferendAFDBis voluptatibus odit veniam consequatur aspernatur dicta veritatis porro, aliquam ratione, praesentium dolorem sint. Exercitationem, corrupti error laboriosam ea dolore unde cupiditate quis reprehenderit voluptate doloribus similique id maiores, nostrum aliquAFDBAFDBAFDBid facere nisi. Neque accusamus ullam aspernatur doloremque vitae cupiditate ab quos recusandae dignissimos facilis nobis, eius expedita fugit sunt suscipit, eaque consectetur tempore harum quis, distinctio quas quia quaerat? Asperiores doloribus voluptates aliquam, nihil enim unde, aspernatur corrupti, exercitationem dolorum expedita quibusdam? Est molestiae esse ratione dicta velit necessitatibus ducimus beatae consectetur! Porro dolore, minima doloribus repudiandae, unde autem atque in adipisci assumenda pariatur temporibus, quisquam sunt eos corporis officia quod deleniti ipsa beatae. Nisi AFDBillo, a optio possimus iure, eaque eligendi porro repudiandae assumenda, omnis quaerat. Nisi libero iure natus tempora earum. Natus eius placeat veritatis eum ipsum non tempora tempore ducimus AFDBvoluptates ratione. Ipsam fugiat provident debitis quis, esse, omnis sapiente velit veritatis impedit, nemo laboriosam sit neque mollitia iure harum itaque qui delectus voluptatem aut dolorem quasi voluptas voluptates cum libero? Reprehenderit magnam asperiores aut omnis architecto doloremque laboriosam ducimus nihil animi eum, odit corrupti deserunt at reiciendis quam molestias dolorem obcaecati? Incidunt, delectus eum ullam saepe, odit dolor dolores blanditiis est quia expedita ipsum, mollitia reiciendis? Voluptatem, dolores possimus animi, vero cumque sequi ducimus delectus ab tempora, iusto aut nulla autem laudantium excepturi deleniti corporis amet hiAFDBAFDBAFDBc. Recusandae sunt vel nesciunt itaque numquam voluptateAFDBm, aliquam culpa dolorum excepturAFDBi necessitatibus dolore atque sit explicabo deleniti, temporibus inventore voluptatum in? Fugiat officia facere beatae? At dolorum eveniet reiciendis corporis fuga eius, non aut consequuntur delectus quidem, blanditiis nesciunt minus hic? Repellendus omnis quas distinctio ullam earum nisi inventore maiores similique sint nam nostrum provident, voluptatibus eius porro magnam molestias perferendis tempore officiis ipsa labore. Ut consequuntur, eaque quasi sapiente laboriosam veniam perferendis earum maxime iure fugiat dolore iste quam dolorum sit hic odio molestiae AFDBAFDBAFDBunde quod porro quaerat! Aliquid maiores alias quaerat AFDBAFDBAFDBmaxime, delectus at. Quam consequatur eligendi natus nesciunt, iste nihil cum reiciendis accusantium ullam soluta ratione eius, voluptate dolores, temporibus pariatur quos. Corporis dolorem provident AFDBAFDBAFDBculpa nobis animi amet! Et ullam beatae ducimus dolorum, rerum quae odit voluptatem sit cupiditate ea qui quasi hic aperiam? Sapiente sint corporis accusamus temporibus molestiae neque nesciunt quasi expedita recusandae aliquid commodi modi exercitationem odit possimus, cum molestias enim minima voluptate explicabo perferendis esse voluptatibus alias debitis numquam! Assumenda perferendis quo, aspernatur doloribus odit perspiciatis cumque nostrum optio temporibus nemo.AFDBAFDBAFDB'
substring = 'AFDBAFDBAFDB'
