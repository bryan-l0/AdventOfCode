#include "adventofcode.h"

vector<string> readInput(string fileName)
{
    ifstream file(fileName);
    string line;
    vector<string> output;
    while (getline(file, line))
    {
        output.push_back(line);
    }
    return output;
}

vector<string_view> splitToVector(string_view input, string token)
{
    vector<string_view> output;
    size_t pointer = 0, tokenPos = 0;
    while ((pointer = input.find_first_not_of(token, tokenPos)) != string_view::npos)
    {
        tokenPos = input.find_first_of(token, pointer);
        output.push_back(input.substr(pointer, tokenPos - pointer));
    }
    return output;
}

unordered_set<string_view> splitToSet(string_view input, string_view token)
{
    unordered_set<string_view> output;
    size_t pointer = 0, tokenPos = 0;
    while ((pointer = input.find_first_not_of(token, tokenPos)) != string_view::npos)
    {
        tokenPos = input.find_first_of(token, pointer);
        output.insert(input.substr(pointer, tokenPos - pointer));
    }
    return output;
}

string_view lstrip(string_view input, string_view token)
{
    size_t tokenPos = input.find_first_of(token);
    tokenPos = input.find_first_not_of(token, tokenPos);
    if (tokenPos == string_view::npos)
        return "";
    return input.substr(tokenPos, input.length());
}

string_view rstrip(string_view input, string_view token)
{
    size_t tokenPos = input.find_last_of(token);
    tokenPos = input.find_last_not_of(token, tokenPos);
    if (tokenPos == string_view::npos)
        return "";
    return input.substr(0, tokenPos + 1);
}
