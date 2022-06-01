
from module import *
from afnSimulator2 import *
combinedAF = AF(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'],['C', 'T', 'm', 'Z', 'F', 'G', 'I', 's', 'i', 'B', 'O', 'Y', 'z', '9', 'j', 'D', 'P', '7', 'a', 'f', 'v', 'e', 'w', 'M', 'p', '4', 'H', 'l', 'b', 'c', 'K', 'L', 'N', 'r', 'g', 't', 'V', 'q', 'X', 'y', '8', 'U', 'x', 'S', 'n', 'o', 'k', 'R', '3', 'A', 'h', 'W', 'u', '2', '6', '1', 'd', 'Q', 'J', 'E', '5', '0', '║', ' ', '╝', '╦'],[['0', 'ε', '1'],['1', 'a', '2'],['1', 'b', '2'],['1', 'c', '2'],['1', 'd', '2'],['1', 'e', '2'],['1', 'f', '2'],['1', 'g', '2'],['1', 'h', '2'],['1', 'i', '4'],['1', 'j', '4'],['1', 'k', '4'],['1', 'l', '4'],['1', 'm', '4'],['1', 'n', '4'],['1', 'o', '4'],['1', 'p', '4'],['1', 'q', '4'],['1', 'r', '4'],['1', 's', '2'],['1', 't', '4'],['1', 'u', '2'],['1', 'v', '2'],['1', 'w', '2'],['1', 'x', '2'],['1', 'y', '2'],['1', 'z', '2'],['1', 'A', '2'],['1', 'B', '2'],['1', 'C', '2'],['1', 'D', '4'],['1', 'E', '2'],['1', 'F', '2'],['1', 'G', '2'],['1', 'H', '2'],['1', 'I', '2'],['1', 'J', '2'],['1', 'K', '2'],['1', 'L', '2'],['1', 'M', '2'],['1', 'N', '4'],['1', 'O', '2'],['1', 'P', '2'],['1', 'Q', '2'],['1', 'R', '2'],['1', 'S', '2'],['1', 'T', '2'],['1', 'U', '2'],['1', 'V', '2'],['1', 'W', '2'],['1', 'X', '4'],['1', 'Y', '2'],['1', 'Z', '2'],['1', '0', '3'],['1', '1', '3'],['1', '2', '3'],['1', '3', '3'],['1', '4', '3'],['1', '5', '3'],['1', '6', '3'],['1', '7', '3'],['1', '8', '3'],['1', '9', '3'],['2', 'a', '2'],['2', 'b', '2'],['2', 'c', '2'],['2', 'd', '2'],['2', 'e', '2'],['2', 'f', '2'],['2', 'g', '4'],['2', 'h', '2'],['2', 'i', '2'],['2', 'j', '2'],['2', 'k', '2'],['2', 'l', '2'],['2', 'm', '2'],['2', 'n', '2'],['2', 'o', '2'],['2', 'p', '2'],['2', 'q', '4'],['2', 'r', '2'],['2', 's', '2'],['2', 't', '2'],['2', 'u', '2'],['2', 'v', '2'],['2', 'w', '2'],['2', 'x', '2'],['2', 'y', '2'],['2', 'z', '2'],['2', 'A', '4'],['2', 'B', '2'],['2', 'C', '2'],['2', 'D', '2'],['2', 'E', '2'],['2', 'F', '2'],['2', 'G', '2'],['2', 'H', '2'],['2', 'I', '2'],['2', 'J', '2'],['2', 'K', '4'],['2', 'L', '2'],['2', 'M', '2'],['2', 'N', '2'],['2', 'O', '2'],['2', 'P', '2'],['2', 'Q', '2'],['2', 'R', '2'],['2', 'S', '2'],['2', 'T', '4'],['2', 'U', '4'],['2', 'V', '4'],['2', 'W', '4'],['2', 'X', '4'],['2', 'Y', '4'],['2', 'Z', '4'],['2', '0', '4'],['2', '1', '4'],['2', '2', '4'],['2', '3', '4'],['2', '4', '4'],['2', '5', '4'],['2', '6', '4'],['2', '7', '4'],['2', '8', '4'],['2', '9', '4'],['4', 'a', '2'],['4', 'b', '2'],['4', 'c', '2'],['4', 'd', '2'],['4', 'e', '2'],['4', 'f', '2'],['4', 'g', '4'],['4', 'h', '2'],['4', 'i', '2'],['4', 'j', '2'],['4', 'k', '2'],['4', 'l', '2'],['4', 'm', '2'],['4', 'n', '2'],['4', 'o', '2'],['4', 'p', '2'],['4', 'q', '4'],['4', 'r', '2'],['4', 's', '2'],['4', 't', '2'],['4', 'u', '2'],['4', 'v', '2'],['4', 'w', '2'],['4', 'x', '2'],['4', 'y', '2'],['4', 'z', '2'],['4', 'A', '4'],['4', 'B', '2'],['4', 'C', '2'],['4', 'D', '2'],['4', 'E', '2'],['4', 'F', '2'],['4', 'G', '2'],['4', 'H', '2'],['4', 'I', '2'],['4', 'J', '2'],['4', 'K', '4'],['4', 'L', '2'],['4', 'M', '2'],['4', 'N', '2'],['4', 'O', '2'],['4', 'P', '2'],['4', 'Q', '2'],['4', 'R', '2'],['4', 'S', '2'],['4', 'T', '4'],['4', 'U', '4'],['4', 'V', '4'],['4', 'W', '4'],['4', 'X', '4'],['4', 'Y', '4'],['4', 'Z', '4'],['4', '0', '4'],['4', '1', '4'],['4', '2', '4'],['4', '3', '4'],['4', '4', '4'],['4', '5', '4'],['4', '6', '4'],['4', '7', '4'],['4', '8', '4'],['4', '9', '4'],['3', 'a', '3'],['3', 'b', '3'],['3', 'c', '3'],['3', 'd', '3'],['3', 'e', '3'],['3', 'f', '3'],['3', 'g', '3'],['3', 'h', '3'],['3', 'i', '3'],['3', 'j', '3'],['3', 'k', '3'],['3', 'l', '3'],['3', 'm', '3'],['3', 'n', '3'],['3', 'o', '3'],['3', 'p', '3'],['3', 'q', '3'],['3', 'r', '3'],['3', 's', '3'],['3', 't', '3'],['3', 'u', '3'],['3', 'v', '3'],['3', 'w', '3'],['3', 'x', '3'],['3', 'y', '3'],['3', 'z', '3'],['3', 'A', '3'],['3', 'B', '3'],['3', 'C', '3'],['3', 'D', '3'],['3', 'E', '3'],['3', 'F', '3'],['3', 'G', '3'],['3', 'H', '3'],['3', 'I', '3'],['3', 'J', '3'],['3', 'K', '3'],['3', 'L', '3'],['3', 'M', '3'],['3', 'N', '3'],['3', 'O', '3'],['3', 'P', '3'],['3', 'Q', '3'],['3', 'R', '3'],['3', 'S', '3'],['3', 'T', '3'],['3', 'U', '3'],['3', 'V', '3'],['3', 'W', '3'],['3', 'X', '3'],['3', 'Y', '3'],['3', 'Z', '3'],['3', '0', '3'],['3', '1', '3'],['3', '2', '3'],['3', '3', '3'],['3', '4', '3'],['3', '5', '3'],['3', '6', '3'],['3', '7', '3'],['3', '8', '3'],['3', '9', '3'],['1', 'a', '2'],['1', 'b', '2'],['1', 'c', '2'],['1', 'd', '2'],['1', 'e', '2'],['1', 'f', '2'],['1', 'g', '2'],['1', 'h', '2'],['1', 'i', '4'],['1', 'j', '4'],['1', 'k', '4'],['1', 'l', '4'],['1', 'm', '4'],['1', 'n', '4'],['1', 'o', '4'],['1', 'p', '4'],['1', 'q', '4'],['1', 'r', '4'],['1', 's', '2'],['1', 't', '4'],['1', 'u', '2'],['1', 'v', '2'],['1', 'w', '2'],['1', 'x', '2'],['1', 'y', '2'],['1', 'z', '2'],['1', 'A', '2'],['1', 'B', '2'],['1', 'C', '2'],['1', 'D', '4'],['1', 'E', '2'],['1', 'F', '2'],['1', 'G', '2'],['1', 'H', '2'],['1', 'I', '2'],['1', 'J', '2'],['1', 'K', '2'],['1', 'L', '2'],['1', 'M', '2'],['1', 'N', '4'],['1', 'O', '2'],['1', 'P', '2'],['1', 'Q', '2'],['1', 'R', '2'],['1', 'S', '2'],['1', 'T', '2'],['1', 'U', '2'],['1', 'V', '2'],['1', 'W', '2'],['1', 'X', '4'],['1', 'Y', '2'],['1', 'Z', '2'],['1', '0', '3'],['1', '1', '3'],['1', '2', '3'],['1', '3', '3'],['1', '4', '3'],['1', '5', '3'],['1', '6', '3'],['1', '7', '3'],['1', '8', '3'],['1', '9', '3'],['2', 'a', '2'],['2', 'b', '2'],['2', 'c', '2'],['2', 'd', '2'],['2', 'e', '2'],['2', 'f', '2'],['2', 'g', '4'],['2', 'h', '2'],['2', 'i', '2'],['2', 'j', '2'],['2', 'k', '2'],['2', 'l', '2'],['2', 'm', '2'],['2', 'n', '2'],['2', 'o', '2'],['2', 'p', '2'],['2', 'q', '4'],['2', 'r', '2'],['2', 's', '2'],['2', 't', '2'],['2', 'u', '2'],['2', 'v', '2'],['2', 'w', '2'],['2', 'x', '2'],['2', 'y', '2'],['2', 'z', '2'],['2', 'A', '4'],['2', 'B', '2'],['2', 'C', '2'],['2', 'D', '2'],['2', 'E', '2'],['2', 'F', '2'],['2', 'G', '2'],['2', 'H', '2'],['2', 'I', '2'],['2', 'J', '2'],['2', 'K', '4'],['2', 'L', '2'],['2', 'M', '2'],['2', 'N', '2'],['2', 'O', '2'],['2', 'P', '2'],['2', 'Q', '2'],['2', 'R', '2'],['2', 'S', '2'],['2', 'T', '4'],['2', 'U', '4'],['2', 'V', '4'],['2', 'W', '4'],['2', 'X', '4'],['2', 'Y', '4'],['2', 'Z', '4'],['2', '0', '4'],['2', '1', '4'],['2', '2', '4'],['2', '3', '4'],['2', '4', '4'],['2', '5', '4'],['2', '6', '4'],['2', '7', '4'],['2', '8', '4'],['2', '9', '4'],['4', 'a', '2'],['4', 'b', '2'],['4', 'c', '2'],['4', 'd', '2'],['4', 'e', '2'],['4', 'f', '2'],['4', 'g', '4'],['4', 'h', '2'],['4', 'i', '2'],['4', 'j', '2'],['4', 'k', '2'],['4', 'l', '2'],['4', 'm', '2'],['4', 'n', '2'],['4', 'o', '2'],['4', 'p', '2'],['4', 'q', '4'],['4', 'r', '2'],['4', 's', '2'],['4', 't', '2'],['4', 'u', '2'],['4', 'v', '2'],['4', 'w', '2'],['4', 'x', '2'],['4', 'y', '2'],['4', 'z', '2'],['4', 'A', '4'],['4', 'B', '2'],['4', 'C', '2'],['4', 'D', '2'],['4', 'E', '2'],['4', 'F', '2'],['4', 'G', '2'],['4', 'H', '2'],['4', 'I', '2'],['4', 'J', '2'],['4', 'K', '4'],['4', 'L', '2'],['4', 'M', '2'],['4', 'N', '2'],['4', 'O', '2'],['4', 'P', '2'],['4', 'Q', '2'],['4', 'R', '2'],['4', 'S', '2'],['4', 'T', '4'],['4', 'U', '4'],['4', 'V', '4'],['4', 'W', '4'],['4', 'X', '4'],['4', 'Y', '4'],['4', 'Z', '4'],['4', '0', '4'],['4', '1', '4'],['4', '2', '4'],['4', '3', '4'],['4', '4', '4'],['4', '5', '4'],['4', '6', '4'],['4', '7', '4'],['4', '8', '4'],['4', '9', '4'],['3', 'a', '3'],['3', 'b', '3'],['3', 'c', '3'],['3', 'd', '3'],['3', 'e', '3'],['3', 'f', '3'],['3', 'g', '3'],['3', 'h', '3'],['3', 'i', '3'],['3', 'j', '3'],['3', 'k', '3'],['3', 'l', '3'],['3', 'm', '3'],['3', 'n', '3'],['3', 'o', '3'],['3', 'p', '3'],['3', 'q', '3'],['3', 'r', '3'],['3', 's', '3'],['3', 't', '3'],['3', 'u', '3'],['3', 'v', '3'],['3', 'w', '3'],['3', 'x', '3'],['3', 'y', '3'],['3', 'z', '3'],['3', 'A', '3'],['3', 'B', '3'],['3', 'C', '3'],['3', 'D', '3'],['3', 'E', '3'],['3', 'F', '3'],['3', 'G', '3'],['3', 'H', '3'],['3', 'I', '3'],['3', 'J', '3'],['3', 'K', '3'],['3', 'L', '3'],['3', 'M', '3'],['3', 'N', '3'],['3', 'O', '3'],['3', 'P', '3'],['3', 'Q', '3'],['3', 'R', '3'],['3', 'S', '3'],['3', 'T', '3'],['3', 'U', '3'],['3', 'V', '3'],['3', 'W', '3'],['3', 'X', '3'],['3', 'Y', '3'],['3', 'Z', '3'],['3', '0', '3'],['3', '1', '3'],['3', '2', '3'],['3', '3', '3'],['3', '4', '3'],['3', '5', '3'],['3', '6', '3'],['3', '7', '3'],['3', '8', '3'],['3', '9', '3'],['1', 'a', '2'],['1', 'b', '2'],['1', 'c', '2'],['1', 'd', '2'],['1', 'e', '2'],['1', 'f', '2'],['1', 'g', '2'],['1', 'h', '2'],['1', 'i', '4'],['1', 'j', '4'],['1', 'k', '4'],['1', 'l', '4'],['1', 'm', '4'],['1', 'n', '4'],['1', 'o', '4'],['1', 'p', '4'],['1', 'q', '4'],['1', 'r', '4'],['1', 's', '2'],['1', 't', '4'],['1', 'u', '2'],['1', 'v', '2'],['1', 'w', '2'],['1', 'x', '2'],['1', 'y', '2'],['1', 'z', '2'],['1', 'A', '2'],['1', 'B', '2'],['1', 'C', '2'],['1', 'D', '4'],['1', 'E', '2'],['1', 'F', '2'],['1', 'G', '2'],['1', 'H', '2'],['1', 'I', '2'],['1', 'J', '2'],['1', 'K', '2'],['1', 'L', '2'],['1', 'M', '2'],['1', 'N', '4'],['1', 'O', '2'],['1', 'P', '2'],['1', 'Q', '2'],['1', 'R', '2'],['1', 'S', '2'],['1', 'T', '2'],['1', 'U', '2'],['1', 'V', '2'],['1', 'W', '2'],['1', 'X', '4'],['1', 'Y', '2'],['1', 'Z', '2'],['1', '0', '3'],['1', '1', '3'],['1', '2', '3'],['1', '3', '3'],['1', '4', '3'],['1', '5', '3'],['1', '6', '3'],['1', '7', '3'],['1', '8', '3'],['1', '9', '3'],['2', 'a', '2'],['2', 'b', '2'],['2', 'c', '2'],['2', 'd', '2'],['2', 'e', '2'],['2', 'f', '2'],['2', 'g', '4'],['2', 'h', '2'],['2', 'i', '2'],['2', 'j', '2'],['2', 'k', '2'],['2', 'l', '2'],['2', 'm', '2'],['2', 'n', '2'],['2', 'o', '2'],['2', 'p', '2'],['2', 'q', '4'],['2', 'r', '2'],['2', 's', '2'],['2', 't', '2'],['2', 'u', '2'],['2', 'v', '2'],['2', 'w', '2'],['2', 'x', '2'],['2', 'y', '2'],['2', 'z', '2'],['2', 'A', '4'],['2', 'B', '2'],['2', 'C', '2'],['2', 'D', '2'],['2', 'E', '2'],['2', 'F', '2'],['2', 'G', '2'],['2', 'H', '2'],['2', 'I', '2'],['2', 'J', '2'],['2', 'K', '4'],['2', 'L', '2'],['2', 'M', '2'],['2', 'N', '2'],['2', 'O', '2'],['2', 'P', '2'],['2', 'Q', '2'],['2', 'R', '2'],['2', 'S', '2'],['2', 'T', '4'],['2', 'U', '4'],['2', 'V', '4'],['2', 'W', '4'],['2', 'X', '4'],['2', 'Y', '4'],['2', 'Z', '4'],['2', '0', '4'],['2', '1', '4'],['2', '2', '4'],['2', '3', '4'],['2', '4', '4'],['2', '5', '4'],['2', '6', '4'],['2', '7', '4'],['2', '8', '4'],['2', '9', '4'],['4', 'a', '2'],['4', 'b', '2'],['4', 'c', '2'],['4', 'd', '2'],['4', 'e', '2'],['4', 'f', '2'],['4', 'g', '4'],['4', 'h', '2'],['4', 'i', '2'],['4', 'j', '2'],['4', 'k', '2'],['4', 'l', '2'],['4', 'm', '2'],['4', 'n', '2'],['4', 'o', '2'],['4', 'p', '2'],['4', 'q', '4'],['4', 'r', '2'],['4', 's', '2'],['4', 't', '2'],['4', 'u', '2'],['4', 'v', '2'],['4', 'w', '2'],['4', 'x', '2'],['4', 'y', '2'],['4', 'z', '2'],['4', 'A', '4'],['4', 'B', '2'],['4', 'C', '2'],['4', 'D', '2'],['4', 'E', '2'],['4', 'F', '2'],['4', 'G', '2'],['4', 'H', '2'],['4', 'I', '2'],['4', 'J', '2'],['4', 'K', '4'],['4', 'L', '2'],['4', 'M', '2'],['4', 'N', '2'],['4', 'O', '2'],['4', 'P', '2'],['4', 'Q', '2'],['4', 'R', '2'],['4', 'S', '2'],['4', 'T', '4'],['4', 'U', '4'],['4', 'V', '4'],['4', 'W', '4'],['4', 'X', '4'],['4', 'Y', '4'],['4', 'Z', '4'],['4', '0', '4'],['4', '1', '4'],['4', '2', '4'],['4', '3', '4'],['4', '4', '4'],['4', '5', '4'],['4', '6', '4'],['4', '7', '4'],['4', '8', '4'],['4', '9', '4'],['3', 'a', '3'],['3', 'b', '3'],['3', 'c', '3'],['3', 'd', '3'],['3', 'e', '3'],['3', 'f', '3'],['3', 'g', '3'],['3', 'h', '3'],['3', 'i', '3'],['3', 'j', '3'],['3', 'k', '3'],['3', 'l', '3'],['3', 'm', '3'],['3', 'n', '3'],['3', 'o', '3'],['3', 'p', '3'],['3', 'q', '3'],['3', 'r', '3'],['3', 's', '3'],['3', 't', '3'],['3', 'u', '3'],['3', 'v', '3'],['3', 'w', '3'],['3', 'x', '3'],['3', 'y', '3'],['3', 'z', '3'],['3', 'A', '3'],['3', 'B', '3'],['3', 'C', '3'],['3', 'D', '3'],['3', 'E', '3'],['3', 'F', '3'],['3', 'G', '3'],['3', 'H', '3'],['3', 'I', '3'],['3', 'J', '3'],['3', 'K', '3'],['3', 'L', '3'],['3', 'M', '3'],['3', 'N', '3'],['3', 'O', '3'],['3', 'P', '3'],['3', 'Q', '3'],['3', 'R', '3'],['3', 'S', '3'],['3', 'T', '3'],['3', 'U', '3'],['3', 'V', '3'],['3', 'W', '3'],['3', 'X', '3'],['3', 'Y', '3'],['3', 'Z', '3'],['3', '0', '3'],['3', '1', '3'],['3', '2', '3'],['3', '3', '3'],['3', '4', '3'],['3', '5', '3'],['3', '6', '3'],['3', '7', '3'],['3', '8', '3'],['3', '9', '3'],['1', 'a', '2'],['1', 'b', '2'],['1', 'c', '2'],['1', 'd', '2'],['1', 'e', '2'],['1', 'f', '2'],['1', 'g', '2'],['1', 'h', '2'],['1', 'i', '4'],['1', 'j', '4'],['1', 'k', '4'],['1', 'l', '4'],['1', 'm', '4'],['1', 'n', '4'],['1', 'o', '4'],['1', 'p', '4'],['1', 'q', '4'],['1', 'r', '4'],['1', 's', '2'],['1', 't', '4'],['1', 'u', '2'],['1', 'v', '2'],['1', 'w', '2'],['1', 'x', '2'],['1', 'y', '2'],['1', 'z', '2'],['1', 'A', '2'],['1', 'B', '2'],['1', 'C', '2'],['1', 'D', '4'],['1', 'E', '2'],['1', 'F', '2'],['1', 'G', '2'],['1', 'H', '2'],['1', 'I', '2'],['1', 'J', '2'],['1', 'K', '2'],['1', 'L', '2'],['1', 'M', '2'],['1', 'N', '4'],['1', 'O', '2'],['1', 'P', '2'],['1', 'Q', '2'],['1', 'R', '2'],['1', 'S', '2'],['1', 'T', '2'],['1', 'U', '2'],['1', 'V', '2'],['1', 'W', '2'],['1', 'X', '4'],['1', 'Y', '2'],['1', 'Z', '2'],['1', '0', '3'],['1', '1', '3'],['1', '2', '3'],['1', '3', '3'],['1', '4', '3'],['1', '5', '3'],['1', '6', '3'],['1', '7', '3'],['1', '8', '3'],['1', '9', '3'],['2', 'a', '2'],['2', 'b', '2'],['2', 'c', '2'],['2', 'd', '2'],['2', 'e', '2'],['2', 'f', '2'],['2', 'g', '4'],['2', 'h', '2'],['2', 'i', '2'],['2', 'j', '2'],['2', 'k', '2'],['2', 'l', '2'],['2', 'm', '2'],['2', 'n', '2'],['2', 'o', '2'],['2', 'p', '2'],['2', 'q', '4'],['2', 'r', '2'],['2', 's', '2'],['2', 't', '2'],['2', 'u', '2'],['2', 'v', '2'],['2', 'w', '2'],['2', 'x', '2'],['2', 'y', '2'],['2', 'z', '2'],['2', 'A', '4'],['2', 'B', '2'],['2', 'C', '2'],['2', 'D', '2'],['2', 'E', '2'],['2', 'F', '2'],['2', 'G', '2'],['2', 'H', '2'],['2', 'I', '2'],['2', 'J', '2'],['2', 'K', '4'],['2', 'L', '2'],['2', 'M', '2'],['2', 'N', '2'],['2', 'O', '2'],['2', 'P', '2'],['2', 'Q', '2'],['2', 'R', '2'],['2', 'S', '2'],['2', 'T', '4'],['2', 'U', '4'],['2', 'V', '4'],['2', 'W', '4'],['2', 'X', '4'],['2', 'Y', '4'],['2', 'Z', '4'],['2', '0', '4'],['2', '1', '4'],['2', '2', '4'],['2', '3', '4'],['2', '4', '4'],['2', '5', '4'],['2', '6', '4'],['2', '7', '4'],['2', '8', '4'],['2', '9', '4'],['4', 'a', '2'],['4', 'b', '2'],['4', 'c', '2'],['4', 'd', '2'],['4', 'e', '2'],['4', 'f', '2'],['4', 'g', '4'],['4', 'h', '2'],['4', 'i', '2'],['4', 'j', '2'],['4', 'k', '2'],['4', 'l', '2'],['4', 'm', '2'],['4', 'n', '2'],['4', 'o', '2'],['4', 'p', '2'],['4', 'q', '4'],['4', 'r', '2'],['4', 's', '2'],['4', 't', '2'],['4', 'u', '2'],['4', 'v', '2'],['4', 'w', '2'],['4', 'x', '2'],['4', 'y', '2'],['4', 'z', '2'],['4', 'A', '4'],['4', 'B', '2'],['4', 'C', '2'],['4', 'D', '2'],['4', 'E', '2'],['4', 'F', '2'],['4', 'G', '2'],['4', 'H', '2'],['4', 'I', '2'],['4', 'J', '2'],['4', 'K', '4'],['4', 'L', '2'],['4', 'M', '2'],['4', 'N', '2'],['4', 'O', '2'],['4', 'P', '2'],['4', 'Q', '2'],['4', 'R', '2'],['4', 'S', '2'],['4', 'T', '4'],['4', 'U', '4'],['4', 'V', '4'],['4', 'W', '4'],['4', 'X', '4'],['4', 'Y', '4'],['4', 'Z', '4'],['4', '0', '4'],['4', '1', '4'],['4', '2', '4'],['4', '3', '4'],['4', '4', '4'],['4', '5', '4'],['4', '6', '4'],['4', '7', '4'],['4', '8', '4'],['4', '9', '4'],['3', 'a', '3'],['3', 'b', '3'],['3', 'c', '3'],['3', 'd', '3'],['3', 'e', '3'],['3', 'f', '3'],['3', 'g', '3'],['3', 'h', '3'],['3', 'i', '3'],['3', 'j', '3'],['3', 'k', '3'],['3', 'l', '3'],['3', 'm', '3'],['3', 'n', '3'],['3', 'o', '3'],['3', 'p', '3'],['3', 'q', '3'],['3', 'r', '3'],['3', 's', '3'],['3', 't', '3'],['3', 'u', '3'],['3', 'v', '3'],['3', 'w', '3'],['3', 'x', '3'],['3', 'y', '3'],['3', 'z', '3'],['3', 'A', '3'],['3', 'B', '3'],['3', 'C', '3'],['3', 'D', '3'],['3', 'E', '3'],['3', 'F', '3'],['3', 'G', '3'],['3', 'H', '3'],['3', 'I', '3'],['3', 'J', '3'],['3', 'K', '3'],['3', 'L', '3'],['3', 'M', '3'],['3', 'N', '3'],['3', 'O', '3'],['3', 'P', '3'],['3', 'Q', '3'],['3', 'R', '3'],['3', 'S', '3'],['3', 'T', '3'],['3', 'U', '3'],['3', 'V', '3'],['3', 'W', '3'],['3', 'X', '3'],['3', 'Y', '3'],['3', 'Z', '3'],['3', '0', '3'],['3', '1', '3'],['3', '2', '3'],['3', '3', '3'],['3', '4', '3'],['3', '5', '3'],['3', '6', '3'],['3', '7', '3'],['3', '8', '3'],['3', '9', '3'],['6', '0', '5'],['6', '1', '5'],['6', '2', '5'],['6', '3', '5'],['6', '4', '5'],['6', '5', '5'],['6', '6', '5'],['6', '7', '5'],['6', '8', '6'],['6', '9', '6'],['6', 'A', '6'],['6', 'B', '6'],['6', 'C', '6'],['6', 'D', '6'],['6', 'E', '6'],['6', 'F', '6'],['6', 'H', '6'],['5', '0', '6'],['5', '1', '5'],['5', '2', '6'],['5', '3', '5'],['5', '4', '5'],['5', '5', '5'],['5', '6', '5'],['5', '7', '5'],['5', '8', '5'],['5', '9', '5'],['5', 'A', '5'],['5', 'B', '5'],['5', 'C', '6'],['5', 'D', '5'],['5', 'E', '5'],['5', 'F', '5'],['5', 'H', '7'],['6', '0', '6'],['6', '2', '6'],['6', '8', '5'],['6', '9', '5'],['6', 'A', '5'],['6', 'B', '5'],['6', 'D', '5'],['6', 'E', '5'],['6', 'F', '5'],['6', 'H', '7'],['6', '1', '6'],['6', '3', '6'],['6', '4', '6'],['6', '5', '6'],['6', '6', '6'],['6', '7', '6'],['7', '0', '6'],['7', '1', '6'],['7', '2', '6'],['7', '3', '6'],['7', '4', '6'],['7', '5', '6'],['7', '6', '6'],['7', '7', '6'],['7', '8', '6'],['7', '9', '6'],['7', 'A', '6'],['7', 'B', '6'],['7', 'C', '6'],['7', 'D', '6'],['7', 'E', '6'],['7', 'F', '6'],['7', 'H', '6'],['0', 'ε', '6'],['6', '0', '5'],['6', '1', '5'],['6', '2', '5'],['6', '3', '5'],['6', '4', '5'],['6', '5', '5'],['6', '6', '5'],['6', '7', '5'],['6', '8', '6'],['6', '9', '6'],['6', 'A', '6'],['6', 'B', '6'],['6', 'C', '6'],['6', 'D', '6'],['6', 'E', '6'],['6', 'F', '6'],['6', 'H', '6'],['5', '0', '6'],['5', '1', '5'],['5', '2', '6'],['5', '3', '5'],['5', '4', '5'],['5', '5', '5'],['5', '6', '5'],['5', '7', '5'],['5', '8', '5'],['5', '9', '5'],['5', 'A', '5'],['5', 'B', '5'],['5', 'C', '6'],['5', 'D', '5'],['5', 'E', '5'],['5', 'F', '5'],['5', 'H', '7'],['6', '0', '6'],['6', '2', '6'],['6', '8', '5'],['6', '9', '5'],['6', 'A', '5'],['6', 'B', '5'],['6', 'D', '5'],['6', 'E', '5'],['6', 'F', '5'],['6', 'H', '7'],['6', '1', '6'],['6', '3', '6'],['6', '4', '6'],['6', '5', '6'],['6', '6', '6'],['6', '7', '6'],['7', '0', '6'],['7', '1', '6'],['7', '2', '6'],['7', '3', '6'],['7', '4', '6'],['7', '5', '6'],['7', '6', '6'],['7', '7', '6'],['7', '8', '6'],['7', '9', '6'],['7', 'A', '6'],['7', 'B', '6'],['7', 'C', '6'],['7', 'D', '6'],['7', 'E', '6'],['7', 'F', '6'],['7', 'H', '6'],['6', '0', '5'],['6', '1', '5'],['6', '2', '5'],['6', '3', '5'],['6', '4', '5'],['6', '5', '5'],['6', '6', '5'],['6', '7', '5'],['6', '8', '6'],['6', '9', '6'],['6', 'A', '6'],['6', 'B', '6'],['6', 'C', '6'],['6', 'D', '6'],['6', 'E', '6'],['6', 'F', '6'],['6', 'H', '6'],['5', '0', '6'],['5', '1', '5'],['5', '2', '6'],['5', '3', '5'],['5', '4', '5'],['5', '5', '5'],['5', '6', '5'],['5', '7', '5'],['5', '8', '5'],['5', '9', '5'],['5', 'A', '5'],['5', 'B', '5'],['5', 'C', '6'],['5', 'D', '5'],['5', 'E', '5'],['5', 'F', '5'],['5', 'H', '7'],['6', '0', '6'],['6', '2', '6'],['6', '8', '5'],['6', '9', '5'],['6', 'A', '5'],['6', 'B', '5'],['6', 'D', '5'],['6', 'E', '5'],['6', 'F', '5'],['6', 'H', '7'],['6', '1', '6'],['6', '3', '6'],['6', '4', '6'],['6', '5', '6'],['6', '6', '6'],['6', '7', '6'],['7', '0', '6'],['7', '1', '6'],['7', '2', '6'],['7', '3', '6'],['7', '4', '6'],['7', '5', '6'],['7', '6', '6'],['7', '7', '6'],['7', '8', '6'],['7', '9', '6'],['7', 'A', '6'],['7', 'B', '6'],['7', 'C', '6'],['7', 'D', '6'],['7', 'E', '6'],['7', 'F', '6'],['7', 'H', '6'],['0', 'ε', '8'],['8', '0', '9'],['8', '1', '9'],['8', '2', '9'],['8', '3', '9'],['8', '4', '9'],['8', '5', '9'],['8', '6', '9'],['8', '7', '9'],['8', '8', '9'],['8', '9', '9'],['9', '0', '9'],['9', '1', '9'],['9', '2', '9'],['9', '3', '9'],['9', '4', '9'],['9', '5', '9'],['9', '6', '9'],['9', '7', '9'],['9', '8', '9'],['9', '9', '9'],['8', '0', '9'],['8', '1', '9'],['8', '2', '9'],['8', '3', '9'],['8', '4', '9'],['8', '5', '9'],['8', '6', '9'],['8', '7', '9'],['8', '8', '9'],['8', '9', '9'],['9', '0', '9'],['9', '1', '9'],['9', '2', '9'],['9', '3', '9'],['9', '4', '9'],['9', '5', '9'],['9', '6', '9'],['9', '7', '9'],['9', '8', '9'],['9', '9', '9'],['12', 's', '15'],['12', 'i', '10'],['12', 'g', '10'],['12', 'n', '10'],['12', '0', '11'],['12', '1', '11'],['12', '2', '11'],['12', '3', '11'],['12', '4', '11'],['12', '5', '11'],['12', '6', '14'],['12', '7', '14'],['12', '8', '14'],['12', '9', '14'],['15', 's', '10'],['15', 'i', '12'],['15', 'g', '10'],['15', 'n', '10'],['15', '0', '10'],['15', '1', '10'],['15', '2', '10'],['15', '3', '10'],['15', '4', '10'],['15', '5', '10'],['15', '6', '10'],['15', '7', '10'],['15', '8', '10'],['15', '9', '10'],['10', 's', '10'],['10', 'i', '10'],['10', 'g', '10'],['10', 'n', '10'],['10', '0', '10'],['10', '1', '10'],['10', '2', '10'],['10', '3', '10'],['10', '4', '10'],['10', '5', '10'],['10', '6', '10'],['10', '7', '10'],['10', '8', '10'],['10', '9', '10'],['11', 's', '10'],['11', 'i', '10'],['11', 'g', '10'],['11', 'n', '10'],['11', '0', '14'],['11', '1', '14'],['11', '2', '14'],['11', '3', '14'],['11', '4', '14'],['11', '5', '13'],['11', '6', '14'],['11', '7', '13'],['11', '8', '13'],['11', '9', '13'],['14', 's', '10'],['14', 'i', '10'],['14', 'g', '10'],['14', 'n', '10'],['14', '0', '14'],['14', '1', '14'],['14', '2', '14'],['14', '3', '14'],['14', '4', '14'],['14', '5', '13'],['14', '6', '14'],['14', '7', '13'],['14', '8', '13'],['14', '9', '13'],['12', 's', '10'],['12', 'g', '15'],['12', '0', '10'],['12', '1', '10'],['12', '2', '10'],['12', '3', '10'],['12', '4', '10'],['12', '5', '10'],['12', '6', '10'],['12', '7', '10'],['12', '8', '10'],['12', '9', '10'],['13', 's', '10'],['13', 'i', '10'],['13', 'g', '10'],['13', 'n', '10'],['13', '0', '14'],['13', '1', '14'],['13', '2', '14'],['13', '3', '14'],['13', '4', '14'],['13', '5', '13'],['13', '6', '14'],['13', '7', '13'],['13', '8', '13'],['13', '9', '13'],['15', 'i', '10'],['15', 'n', '15'],['15', '0', '11'],['15', '1', '11'],['15', '2', '11'],['15', '3', '11'],['15', '4', '11'],['15', '5', '11'],['15', '6', '14'],['15', '7', '14'],['15', '8', '14'],['15', '9', '14'],['12', 's', '15'],['12', 'i', '10'],['12', 'g', '10'],['12', 'n', '10'],['12', '0', '11'],['12', '1', '11'],['12', '2', '11'],['12', '3', '11'],['12', '4', '11'],['12', '5', '11'],['12', '6', '14'],['12', '7', '14'],['12', '8', '14'],['12', '9', '14'],['15', 's', '10'],['15', 'i', '12'],['15', 'g', '10'],['15', 'n', '10'],['15', '0', '10'],['15', '1', '10'],['15', '2', '10'],['15', '3', '10'],['15', '4', '10'],['15', '5', '10'],['15', '6', '10'],['15', '7', '10'],['15', '8', '10'],['15', '9', '10'],['10', 's', '10'],['10', 'i', '10'],['10', 'g', '10'],['10', 'n', '10'],['10', '0', '10'],['10', '1', '10'],['10', '2', '10'],['10', '3', '10'],['10', '4', '10'],['10', '5', '10'],['10', '6', '10'],['10', '7', '10'],['10', '8', '10'],['10', '9', '10'],['11', 's', '10'],['11', 'i', '10'],['11', 'g', '10'],['11', 'n', '10'],['11', '0', '14'],['11', '1', '14'],['11', '2', '14'],['11', '3', '14'],['11', '4', '14'],['11', '5', '13'],['11', '6', '14'],['11', '7', '13'],['11', '8', '13'],['11', '9', '13'],['14', 's', '10'],['14', 'i', '10'],['14', 'g', '10'],['14', 'n', '10'],['14', '0', '14'],['14', '1', '14'],['14', '2', '14'],['14', '3', '14'],['14', '4', '14'],['14', '5', '13'],['14', '6', '14'],['14', '7', '13'],['14', '8', '13'],['14', '9', '13'],['12', 's', '10'],['12', 'g', '15'],['12', '0', '10'],['12', '1', '10'],['12', '2', '10'],['12', '3', '10'],['12', '4', '10'],['12', '5', '10'],['12', '6', '10'],['12', '7', '10'],['12', '8', '10'],['12', '9', '10'],['13', 's', '10'],['13', 'i', '10'],['13', 'g', '10'],['13', 'n', '10'],['13', '0', '14'],['13', '1', '14'],['13', '2', '14'],['13', '3', '14'],['13', '4', '14'],['13', '5', '13'],['13', '6', '14'],['13', '7', '13'],['13', '8', '13'],['13', '9', '13'],['15', 'i', '10'],['15', 'n', '15'],['15', '0', '11'],['15', '1', '11'],['15', '2', '11'],['15', '3', '11'],['15', '4', '11'],['15', '5', '11'],['15', '6', '14'],['15', '7', '14'],['15', '8', '14'],['15', '9', '14'],['0', 'ε', '12'],['12', 's', '15'],['12', 'i', '10'],['12', 'g', '10'],['12', 'n', '10'],['12', '0', '11'],['12', '1', '11'],['12', '2', '11'],['12', '3', '11'],['12', '4', '11'],['12', '5', '11'],['12', '6', '14'],['12', '7', '14'],['12', '8', '14'],['12', '9', '14'],['15', 's', '10'],['15', 'i', '12'],['15', 'g', '10'],['15', 'n', '10'],['15', '0', '10'],['15', '1', '10'],['15', '2', '10'],['15', '3', '10'],['15', '4', '10'],['15', '5', '10'],['15', '6', '10'],['15', '7', '10'],['15', '8', '10'],['15', '9', '10'],['10', 's', '10'],['10', 'i', '10'],['10', 'g', '10'],['10', 'n', '10'],['10', '0', '10'],['10', '1', '10'],['10', '2', '10'],['10', '3', '10'],['10', '4', '10'],['10', '5', '10'],['10', '6', '10'],['10', '7', '10'],['10', '8', '10'],['10', '9', '10'],['11', 's', '10'],['11', 'i', '10'],['11', 'g', '10'],['11', 'n', '10'],['11', '0', '14'],['11', '1', '14'],['11', '2', '14'],['11', '3', '14'],['11', '4', '14'],['11', '5', '13'],['11', '6', '14'],['11', '7', '13'],['11', '8', '13'],['11', '9', '13'],['14', 's', '10'],['14', 'i', '10'],['14', 'g', '10'],['14', 'n', '10'],['14', '0', '14'],['14', '1', '14'],['14', '2', '14'],['14', '3', '14'],['14', '4', '14'],['14', '5', '13'],['14', '6', '14'],['14', '7', '13'],['14', '8', '13'],['14', '9', '13'],['12', 's', '10'],['12', 'g', '15'],['12', '0', '10'],['12', '1', '10'],['12', '2', '10'],['12', '3', '10'],['12', '4', '10'],['12', '5', '10'],['12', '6', '10'],['12', '7', '10'],['12', '8', '10'],['12', '9', '10'],['13', 's', '10'],['13', 'i', '10'],['13', 'g', '10'],['13', 'n', '10'],['13', '0', '14'],['13', '1', '14'],['13', '2', '14'],['13', '3', '14'],['13', '4', '14'],['13', '5', '13'],['13', '6', '14'],['13', '7', '13'],['13', '8', '13'],['13', '9', '13'],['15', 'i', '10'],['15', 'n', '15'],['15', '0', '11'],['15', '1', '11'],['15', '2', '11'],['15', '3', '11'],['15', '4', '11'],['15', '5', '11'],['15', '6', '14'],['15', '7', '14'],['15', '8', '14'],['15', '9', '14'],['12', 's', '15'],['12', 'i', '10'],['12', 'g', '10'],['12', 'n', '10'],['12', '0', '11'],['12', '1', '11'],['12', '2', '11'],['12', '3', '11'],['12', '4', '11'],['12', '5', '11'],['12', '6', '14'],['12', '7', '14'],['12', '8', '14'],['12', '9', '14'],['15', 's', '10'],['15', 'i', '12'],['15', 'g', '10'],['15', 'n', '10'],['15', '0', '10'],['15', '1', '10'],['15', '2', '10'],['15', '3', '10'],['15', '4', '10'],['15', '5', '10'],['15', '6', '10'],['15', '7', '10'],['15', '8', '10'],['15', '9', '10'],['10', 's', '10'],['10', 'i', '10'],['10', 'g', '10'],['10', 'n', '10'],['10', '0', '10'],['10', '1', '10'],['10', '2', '10'],['10', '3', '10'],['10', '4', '10'],['10', '5', '10'],['10', '6', '10'],['10', '7', '10'],['10', '8', '10'],['10', '9', '10'],['11', 's', '10'],['11', 'i', '10'],['11', 'g', '10'],['11', 'n', '10'],['11', '0', '14'],['11', '1', '14'],['11', '2', '14'],['11', '3', '14'],['11', '4', '14'],['11', '5', '13'],['11', '6', '14'],['11', '7', '13'],['11', '8', '13'],['11', '9', '13'],['14', 's', '10'],['14', 'i', '10'],['14', 'g', '10'],['14', 'n', '10'],['14', '0', '14'],['14', '1', '14'],['14', '2', '14'],['14', '3', '14'],['14', '4', '14'],['14', '5', '13'],['14', '6', '14'],['14', '7', '13'],['14', '8', '13'],['14', '9', '13'],['12', 's', '10'],['12', 'g', '15'],['12', '0', '10'],['12', '1', '10'],['12', '2', '10'],['12', '3', '10'],['12', '4', '10'],['12', '5', '10'],['12', '6', '10'],['12', '7', '10'],['12', '8', '10'],['12', '9', '10'],['13', 's', '10'],['13', 'i', '10'],['13', 'g', '10'],['13', 'n', '10'],['13', '0', '14'],['13', '1', '14'],['13', '2', '14'],['13', '3', '14'],['13', '4', '14'],['13', '5', '13'],['13', '6', '14'],['13', '7', '13'],['13', '8', '13'],['13', '9', '13'],['15', 'i', '10'],['15', 'n', '15'],['15', '0', '11'],['15', '1', '11'],['15', '2', '11'],['15', '3', '11'],['15', '4', '11'],['15', '5', '11'],['15', '6', '14'],['15', '7', '14'],['15', '8', '14'],['15', '9', '14'],['12', 's', '15'],['12', 'i', '10'],['12', 'g', '10'],['12', 'n', '10'],['12', '0', '11'],['12', '1', '11'],['12', '2', '11'],['12', '3', '11'],['12', '4', '11'],['12', '5', '11'],['12', '6', '14'],['12', '7', '14'],['12', '8', '14'],['12', '9', '14'],['15', 's', '10'],['15', 'i', '12'],['15', 'g', '10'],['15', 'n', '10'],['15', '0', '10'],['15', '1', '10'],['15', '2', '10'],['15', '3', '10'],['15', '4', '10'],['15', '5', '10'],['15', '6', '10'],['15', '7', '10'],['15', '8', '10'],['15', '9', '10'],['10', 's', '10'],['10', 'i', '10'],['10', 'g', '10'],['10', 'n', '10'],['10', '0', '10'],['10', '1', '10'],['10', '2', '10'],['10', '3', '10'],['10', '4', '10'],['10', '5', '10'],['10', '6', '10'],['10', '7', '10'],['10', '8', '10'],['10', '9', '10'],['11', 's', '10'],['11', 'i', '10'],['11', 'g', '10'],['11', 'n', '10'],['11', '0', '14'],['11', '1', '14'],['11', '2', '14'],['11', '3', '14'],['11', '4', '14'],['11', '5', '13'],['11', '6', '14'],['11', '7', '13'],['11', '8', '13'],['11', '9', '13'],['14', 's', '10'],['14', 'i', '10'],['14', 'g', '10'],['14', 'n', '10'],['14', '0', '14'],['14', '1', '14'],['14', '2', '14'],['14', '3', '14'],['14', '4', '14'],['14', '5', '13'],['14', '6', '14'],['14', '7', '13'],['14', '8', '13'],['14', '9', '13'],['12', 's', '10'],['12', 'g', '15'],['12', '0', '10'],['12', '1', '10'],['12', '2', '10'],['12', '3', '10'],['12', '4', '10'],['12', '5', '10'],['12', '6', '10'],['12', '7', '10'],['12', '8', '10'],['12', '9', '10'],['13', 's', '10'],['13', 'i', '10'],['13', 'g', '10'],['13', 'n', '10'],['13', '0', '14'],['13', '1', '14'],['13', '2', '14'],['13', '3', '14'],['13', '4', '14'],['13', '5', '13'],['13', '6', '14'],['13', '7', '13'],['13', '8', '13'],['13', '9', '13'],['15', 'i', '10'],['15', 'n', '15'],['15', '0', '11'],['15', '1', '11'],['15', '2', '11'],['15', '3', '11'],['15', '4', '11'],['15', '5', '11'],['15', '6', '14'],['15', '7', '14'],['15', '8', '14'],['15', '9', '14'],['12', 's', '15'],['12', 'i', '10'],['12', 'g', '10'],['12', 'n', '10'],['12', '0', '11'],['12', '1', '11'],['12', '2', '11'],['12', '3', '11'],['12', '4', '11'],['12', '5', '11'],['12', '6', '14'],['12', '7', '14'],['12', '8', '14'],['12', '9', '14'],['15', 's', '10'],['15', 'i', '12'],['15', 'g', '10'],['15', 'n', '10'],['15', '0', '10'],['15', '1', '10'],['15', '2', '10'],['15', '3', '10'],['15', '4', '10'],['15', '5', '10'],['15', '6', '10'],['15', '7', '10'],['15', '8', '10'],['15', '9', '10'],['10', 's', '10'],['10', 'i', '10'],['10', 'g', '10'],['10', 'n', '10'],['10', '0', '10'],['10', '1', '10'],['10', '2', '10'],['10', '3', '10'],['10', '4', '10'],['10', '5', '10'],['10', '6', '10'],['10', '7', '10'],['10', '8', '10'],['10', '9', '10'],['11', 's', '10'],['11', 'i', '10'],['11', 'g', '10'],['11', 'n', '10'],['11', '0', '14'],['11', '1', '14'],['11', '2', '14'],['11', '3', '14'],['11', '4', '14'],['11', '5', '13'],['11', '6', '14'],['11', '7', '13'],['11', '8', '13'],['11', '9', '13'],['14', 's', '10'],['14', 'i', '10'],['14', 'g', '10'],['14', 'n', '10'],['14', '0', '14'],['14', '1', '14'],['14', '2', '14'],['14', '3', '14'],['14', '4', '14'],['14', '5', '13'],['14', '6', '14'],['14', '7', '13'],['14', '8', '13'],['14', '9', '13'],['12', 's', '10'],['12', 'g', '15'],['12', '0', '10'],['12', '1', '10'],['12', '2', '10'],['12', '3', '10'],['12', '4', '10'],['12', '5', '10'],['12', '6', '10'],['12', '7', '10'],['12', '8', '10'],['12', '9', '10'],['13', 's', '10'],['13', 'i', '10'],['13', 'g', '10'],['13', 'n', '10'],['13', '0', '14'],['13', '1', '14'],['13', '2', '14'],['13', '3', '14'],['13', '4', '14'],['13', '5', '13'],['13', '6', '14'],['13', '7', '13'],['13', '8', '13'],['13', '9', '13'],['15', 'i', '10'],['15', 'n', '15'],['15', '0', '11'],['15', '1', '11'],['15', '2', '11'],['15', '3', '11'],['15', '4', '11'],['15', '5', '11'],['15', '6', '14'],['15', '7', '14'],['15', '8', '14'],['15', '9', '14'],['0', 'ε', '16'],['16', '╝', '17'],['16', '║', '17'],['16', '╦', '17'],['16', ' ', '17'],['17', '╝', '17'],['17', '║', '17'],['17', '╦', '17'],['17', ' ', '17'],['16', '╝', '17'],['16', '║', '17'],['16', '╦', '17'],['16', ' ', '17'],['17', '╝', '17'],['17', '║', '17'],['17', '╦', '17'],['17', ' ', '17']],['0'],['2', '4', '7', '9', '11', '13', '14', '17'])
tokenList = [['0', '2'],['0', '4'],['1', '7'],['2', '9'],['3', '11'],['3', '13'],['3', '14'],['4', '17']]
tokens = [['ident', '(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)((a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)|(0|1|2|3|4|5|6|7|8|9))*'],['hexnumber', '(0|1|2|3|4|5|6|7|8|9|A|B|C|D|E|F)((0|1|2|3|4|5|6|7|8|9|A|B|C|D|E|F))*(H)'],['number', '(0|1|2|3|4|5|6|7|8|9)((0|1|2|3|4|5|6|7|8|9))*'],['signnumber', '(sign)?(0|1|2|3|4|5|6|7|8|9)((0|1|2|3|4|5|6|7|8|9))*'],['whitetoken', '(╝|║|╦| )((╝|║|╦| ))*']]
keys = [['while', 'while'],['do', 'do']]

keyValues = []
for key in keys:
    keyValues.append(key[1])

testFileName = input("Ingrese el nombre del archivo: ")
file = open(testFileName, "r")
lines = file.readlines()

for line in lines:
    response = (afnSimulator2(combinedAF, line, keyValues))

    cont = 0
    for item in response:
        for t in tokenList:
            if (item == t[1]):
                response[cont] = tokens[int(t[0])][0]
        
        cont += 1

    print(response)