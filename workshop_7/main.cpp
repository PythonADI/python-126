#include <iostream>
#include <fstream>

int main() {
    // Open for reading and writing without erasing the file
    std::fstream file("example.txt", std::ios::in | std::ios::out);
    
    if (file.is_open()) {
        // Move the write pointer to the 10th byte
        file.seekp(10);
        
        // Overwrite the next 5 bytes with "HELLO"
        file << "";
        
        file.close();
    }
    return 0;
}
