import os
import heapq

class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value=value
        self.freq=freq
        self.left=None
        self.right=None

    def __lt__(self,other):
        return self.freq<other.freq

    def __eq__(self,other):
        return self.freq==other.freq

class HuffmanCoding:
    
    def __init__(self,path):
        self.path=path
        self.__heap=[]
        self.__codes={}
        self.__reverse_codes={}
        

    def __make_frequency_dict(self,text):
        freq_dict={}
        for char in text:
            if char not in freq_dict:
                freq_dict[char]=0
            freq_dict[char]+=1
        return freq_dict
    

    def __buildHeap(self,freq_dict):
        for key in freq_dict:
            frequency=freq_dict[key]
            binary_tree_node=BinaryTreeNode(key,frequency)
            heapq.heappush(self.__heap,binary_tree_node)
    

    def __buildTree(self):
        while(len(self.__heap)>1):
            binary_tree_node_1=heapq.heappop(self.__heap)
            binary_tree_node_2=heapq.heappop(self.__heap)
            
            freq_sum=binary_tree_node_1.freq+binary_tree_node_2.freq
            newNode=BinaryTreeNode(None,freq_sum)
            
            newNode.left=binary_tree_node_1
            newNode.right=binary_tree_node_2

            heapq.heappush(self.__heap,newNode)
        return
    

    def __buildCodesHelper(self,root,curr_bits):
        if root is None:
            return 
        # If the current node is a leaf node (contains a character)
        if root.value is not None:
            self.__codes[root.value] = curr_bits
            self.__reverse_codes[curr_bits] = root.value
            return
        #appending '0' for left and '1' for right
        self.__buildCodesHelper(root.left,curr_bits+"0")
        self.__buildCodesHelper(root.right,curr_bits+"1")
    

    def __buildCodes(self):
        '''One IMPORTANT thing about all these codes for each of the character is that
            No two charcters will have same prefix
            eg.. if a --> 101 then, none of the else char's Code will start with 101
            '''
        root=heapq.heappop(self.__heap)
        self.__buildCodesHelper(root,"")


    def __getEncodedText(self,text):
        encoded_text=""
        for char in text:
            encoded_text+=self.__codes[char]
        return encoded_text
    

    def __getPaddedEncodedText(self,encoded_text):
        padded_amount=8-(len(encoded_text)%8)
        for i in range(padded_amount):
            encoded_text+='0'
        '''

        "{(p)0 : (q)08b}"
            p --->>> take the first argument of the '.format' function
            q --->>> 'b' tells to convert the padded_amount into binary (eg..   5 -->  101)
                 '08' convert  the binary into 8 digits (eg...  101 -->  00000101)
        '''
        padded_info="{0:08b}".format(padded_amount)
        encoded_text = padded_info+encoded_text
        return encoded_text
    

    def __getBytesArray(self,padded_encoded_text):
        array=[]
        for i in range(0,len(padded_encoded_text),8):
            byte = padded_encoded_text[i:i+8]
            array.append(int(byte,2))
        return array
        
    def compress(self):
        file_name,file_extension=os.path.splitext(self.path)
        output_path=file_name + ".bin"
        try:
            with open(self.path,'r+') as file,open(output_path,'wb')as output:
                text=file.read()
                text=text.rstrip()
                
                freq_dict = self.__make_frequency_dict(text)
                
                self.__buildHeap(freq_dict)
                
                self.__buildTree()
                
                self.__buildCodes()
                
                encoded_text=self.__getEncodedText(text)
                
                padded_encoded_text = self.__getPaddedEncodedText(encoded_text)
                
                bytes_array = self.__getBytesArray(padded_encoded_text)
                final_bytes = bytes(bytes_array)
                output.write(final_bytes)
        except Exception as e:
            print(f'ERROR OCCURRED: {e}')
            exit(1)
        print('Compressed')
        return output_path
    
    def __removePadding(self,text):
        padded_info=text[:8]
        extra_padding=int(padded_info,2)
        text=text[8:]
        text_after_padding_removed=text[:-1*extra_padding]
        return text_after_padding_removed


    def __decodeText(self,text):
        decoded_text=""
        current_bits=""
        for bit in text:
            current_bits+=bit
            if current_bits in self.__reverse_codes:
                character=self.__reverse_codes[current_bits]
                decoded_text += character
                current_bits = ""
        return decoded_text
    
    # Method to decompress the input binary file
    def decompress(self,input_path):
        filename,file_extension=os.path.splitext(input_path)
        output_path=filename + "_decompressed" + ".txt"
        try:
            with open(input_path,'rb') as file:
                output = open(output_path,'w') 
                bit_string=""
                byte=file.read(1)
                while byte:
                    byte=ord(byte)   # bytes to an Integer say 5
                    '''
                    bin(5) -->> gives " b'101  "  and we don't want first two char
                    bin(5)[2:] ---->>> '101'   bt we want 8 bits form of 101
                    .rjust(8, '0) will check for len(bin(5)[2:])... if it is less then 8, will add that many zero in front
                    '''
                    bits=bin(byte)[2:].rjust(8,'0')  # for 5 --->>> bits = 00000101
                    bit_string+=bits
                    byte=file.read(1) # read the next byte
                actual_text=self.__removePadding(bit_string)
                decompressed_text = self.__decodeText(actual_text)
                output.write(decompressed_text)
                output.close()
        except Exception as e:
            print(f"ERROR OCCURED : {e}")
            return
        print('Decompressed')
        return

file_path = "D:/Coding/Python_Data/Codes/DSA_Codes/Huffman_coding/sample_file.txt"
hf = HuffmanCoding(file_path)
op = hf.compress()
hf.decompress(op)