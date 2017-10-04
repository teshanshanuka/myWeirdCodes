// Example progradm
#include <stdint.h>
#include <stdio.h>

#include <iostream>
#include <string>
#include <bitset>


void tox64(uint32_t d1,uint32_t d2,uint32_t d3,uint8_t d4,uint8_t d5);

static char encoding_table[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                                'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                                'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                                'w', 'x', 'y', 'z', '0', '1', '2', '3',
                                '4', '5', '6', '7', '8', '9', '+', '/'};

int main()
{    
    uint32_t a = 0b01001001010011101011010101011111;
    uint32_t b = 0b01101001010010100111000101011001;
    uint32_t c = 0b01001001011001000011000010011011;
    uint8_t d = 0b10101001;
    uint8_t e = 0b01110011;

    // uint32_t a = 63;
    // uint32_t b = 0;
    // uint32_t c = 0;
    // uint8_t d = 0;
    // uint8_t e = 0;
    
    printf(":%d\n:%d\n:%d\n:%d\n:%d\n",a,b,c,d,e);
    tox64(a,b,c,d,e);

}


void tox64(uint32_t d1,uint32_t d2,uint32_t d3,uint8_t d4,uint8_t d5)
{
    uint8_t i;
    uint8_t b64[19];
    char code[19];
        
    for(i=0; i<6;i++)
    {
        b64[i] = (d1 >> i*6) & 0b00111111;
    }
    
    b64[i-1] |= (d2 << 2) & 0b00111111;
    
    for(uint8_t j=0; j<5;j++)
    {
        b64[i] = (d2 >> j*6+4) & 0b00111111;
        i++;
    }

    b64[i-1] |= (d3 << 4) & 0b00111111;
    
    for(uint8_t j=0; j<5;j++)
    {
        b64[i] = (d3 >> j*6+2) & 0b00111111;
        i++;
        // std::cout << std::bitset<8>(b64[i-1])  << std::endl;
    }

    b64[i++] = d4 & 0b00111111;
    b64[i++] = (d4 >> 6 |  d5 << 2) & 0b00111111;
    b64[i] = d5 >> 4 & 0b00111111;
    
    for(uint8_t j=0; j<19;j++)
    {
        // std::cout << std::bitset<8>(b64[j])  << std::endl;
        // std::cout << (int)b64[j];
        // std::cout << " ";
        code[19-j-1] = encoding_table[b64[j]];
    }
    std::cout << "\n";
    printf("%s\n",code);
}
