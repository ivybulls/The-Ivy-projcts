#include <iostream>
#include <string>
#include <unordered_map>

int main() {
    std::string str = "AABBACCDDBDE";
    std::unordered_map<char, int> freqMap;

    for (char c : str) {
        freqMap[c]++;
    }

    for (auto const& [key, val] : freqMap) {
        std::cout << key << ": " << val << std::endl;
    }
    return 0;
}

