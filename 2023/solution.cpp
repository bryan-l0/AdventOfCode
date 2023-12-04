#include "adventofcode.cpp"

int day1solution(vector<string> input, regex re, regex rev)
{
    string replacedLine;
    char firstChar, lastChar;
    int count = 0;
    for (string &line : input)
    {
        replacedLine = regex_replace(line, re, "");
        for (auto it = replacedLine.begin(); it != replacedLine.end(); ++it)
        {
            switch (*it)
            {
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
            {
                firstChar = *it;
                break;
            }
            case 'e':
                firstChar = '8';
                break;
            case 'n':
                firstChar = '9';
                break;
            case 'o':
                firstChar = '1';
                break;
            case 'f':
                ++it;
                if (*it == 'i')
                    firstChar = '5';
                else
                    firstChar = '4';
                break;
            case 's':
                ++it;
                if (*it == 'e')
                    firstChar = '7';
                else
                    firstChar = '6';
                break;
            case 't':
                ++it;
                if (*it == 'h')
                    firstChar = '3';
                else
                    firstChar = '2';
                break;
            }
        }
        reverse(line.begin(), line.end());
        replacedLine = regex_replace(line, rev, "");
        for (auto it = replacedLine.begin(); it != replacedLine.end(); ++it)
        {
            switch (*it)
            {
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
            {
                lastChar = *it;
                break;
            }
            case 'n':
                lastChar = '7';
                break;
            case 'o':
                lastChar = '2';
                break;
            case 'r':
                lastChar = '4';
                break;
            case 't':
                lastChar = '8';
                break;
            case 'x':
                lastChar = 'x';
                break;
            case 'e':
                ++it;
                if (*it == 'e')
                {
                    lastChar = '3';
                }
                else if (*it == 'v')
                {
                    lastChar = '5';
                }
                else
                {
                    ++it;
                    if (*it == 'i')
                        lastChar = '9';
                    else
                        lastChar = '1';
                }
                break;
            }
        }
        count += stoi(string() + firstChar + lastChar);
    }
    return count;
}

void day1()
{
    vector<string> input = readInput("day01in");
    regex partOne("[a-zA-Z]");
    regex partOneReversed("[a-zA-Z]");
    regex partTwo("[a-zA-Z](?!one)(?!two)(?!three)(?!four)(?!five)(?!six)(?!seven)(?!eight)(?!nine)");
    regex partTwoReversed("[a-zA-Z](?!eno)(?!owt)(?!eerht)(?!ruof)(?!evif)(?!xis)(?!neves)(?!thgie)(?!enin)");
    cout << "day1 part1: " << day1solution(input, partOne, partOneReversed) << endl;
    // cout << "Day 1, Part 2: " << day1solution(input, partTwo, partTwoReversed) << endl;
}

int day4part1(vector<string> &input)
{
    unordered_set<string_view> winningNumbers;
    string winningString;
    string_view purchasedNumbersString;
    pair<string, string> splitString;
    vector<string_view> splitStringVector;
    int output = 0, sum = 1;
    for (const string &line : input)
    {
        purchasedNumbersString = lstrip(line, ":");
        splitStringVector = splitToVector(purchasedNumbersString, "|");
        winningNumbers = splitToSet(splitStringVector[1], " ");
        sum = 0;
        for (const string_view &number : splitToSet(splitStringVector[0], " "))
        {
            if (!winningNumbers.contains(number))
                continue;
            if (sum == 0)
                sum = 1;
            else
                sum *= 2;
        }
        output += sum;
    }
    return output;
}

int day4part2(vector<string> &input)
{
    unordered_set<string_view> winningNumbers;
    string winningString;
    string_view purchasedNumbersString;
    pair<string, string> splitString;
    vector<string_view> splitStringVector;
    vector<size_t> runningTotal(input.size(), 1);
    int count, output = 0;
    string line;
    for (size_t lineNumber = 0; lineNumber < input.size(); ++lineNumber)
    {
        line = input[lineNumber];
        purchasedNumbersString = lstrip(line, ":");
        splitStringVector = splitToVector(purchasedNumbersString, "|");
        winningNumbers = splitToSet(splitStringVector[1], " ");
        count = 0;
        for (const string_view &number : splitToSet(splitStringVector[0], " "))
        {
            if (winningNumbers.contains(number))
                ++count;
        }
        for (size_t i = 1; i < input.size() && i < count + 1; ++i) {
            runningTotal[i + lineNumber] += runningTotal[lineNumber];
        }
        output += runningTotal[lineNumber];
    }
    return output;
}

void day4()
{
    vector<string> input = readInput("day04in");
    cout << "day4 part1: " << day4part1(input) << endl;
    cout << "day4 part2: " << day4part2(input) << endl;
}

int main()
{
    day4();
    return 0;
}