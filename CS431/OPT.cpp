//Thomas Saltzman
// OPT project

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;
int find_largest_distance(vector<int>& frames, vector<int>& page_file,int start);
bool in_frames(vector<int>& frames,int page);
void read_in_file(string filename);
void OPT(string& input);
bool check_file_stirng(string input);
bool check_file_name(string filename);


int main(int argc, char *argv[]) {
	if (argc > 1) { 
		string filename = argv[1];
		if (check_file_name(filename))
			read_in_file(filename);
		else
			cout << "this program only works on csv files." << "\n";
	}
    return 0;
}
bool in_frames(vector<int>&frames, int page){
    
  for (int i = 0; i < frames.size(); ++i) {
    if (frames[i] == page)
        return true;
  }
  return false;
}

int find_largest_distance(vector<int>& frames,vector<int>& page_file,int start){

int index = -1;
int distance = -1;
bool found = false;
for(int k = 0; k < frames.size(); ++k)
{    
    for (int i = start; i < page_file.size(); ++i) 
    {
        if (frames[k] == page_file[i])
        {
            found = true;
            if(i > distance){
                distance = i;
                index = k;
            }
            break;
        }
    }
    if(!found) //there are no more of this file type in the string. swap it out.
    {
        index = k;
        break;
    }
    found = false;
    
}
    return index;
}

void read_in_file(string filename) {

	ifstream ist(filename);
	if (ist) {
		string input;
		while (getline(ist, input)) {
			if (check_file_stirng(input))
				OPT(input);
			else
				cout << "file contains a bad line." << "\n";
		}
	}
}
void OPT(string& input){

    vector<int> page_file;
    vector<int> frames;
   
    int fault_count = 0;
    
    int size = input[0] - '0';
    cout<<size<<" ";
	for (int i = 2; i < input.size(); i++) {
		if(isalnum(input[i]))
			page_file.push_back(input[i] - '0');
	}
    
    for (int i = 0; i < page_file.size(); ++i) 
    {
     
        if(!in_frames(frames,page_file[i]))
        {   ++fault_count;
            if(frames.size()< size)
            {
                frames.push_back(page_file[i]);
            }
            else
            {
                frames[find_largest_distance(frames,page_file,i+1)] = page_file[i];
            }
        }
    }
    cout<<fault_count<<endl;
    
}
bool check_file_stirng(string input) {
	return input.find_first_not_of("0123456789, ") == string::npos; // checks to see if the line is only digits, commas, and spaces
}

bool check_file_name(string filename) {
	return (filename.substr(filename.length() - 3) == "csv");
}