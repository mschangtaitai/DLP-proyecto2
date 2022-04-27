
from module import *
from afnSimulator2 import *
combinedAF = AF(['0', '1', '2', '3', '4', '5', '6'],['A', '4', 'p', 'E', 'N', '1', 'z', 'c', '6', 'r', 'u', 'I', '0', 'n', 'F', '5', 'd', 'v', 'C', 'e', 'H', 'l', '7', 'j', '3', 'K', 'a', 'P', 'Y', 't', 'x', 'w', 'Q', 'B', 'L', 'X', 'b', 'S', 'f', 'D', 'h', 's', '2', 'k', 'q', 'V', 'g', 'G', 'i', 'U', 'm', 'R', 'O', 'J', 'o', 'Z', 'y', 'T', 'M', '9', '8', 'W'],[['0', 'ε', '1'],['1', 'A', '2'],['1', 'B', '2'],['1', 'C', '2'],['1', 'D', '2'],['1', 'E', '2'],['1', 'F', '2'],['1', 'G', '2'],['1', 'H', '2'],['1', 'I', '4'],['1', 'J', '4'],['1', 'K', '4'],['1', 'L', '4'],['1', 'M', '4'],['1', 'N', '4'],['1', 'O', '4'],['1', 'P', '4'],['1', 'Q', '4'],['1', 'R', '4'],['1', 'S', '2'],['1', 'T', '4'],['1', 'U', '2'],['1', 'V', '2'],['1', 'W', '2'],['1', 'X', '2'],['1', 'Y', '2'],['1', 'Z', '2'],['1', 'a', '2'],['1', 'b', '2'],['1', 'c', '2'],['1', 'd', '4'],['1', 'e', '2'],['1', 'f', '2'],['1', 'g', '2'],['1', 'h', '2'],['1', 'i', '2'],['1', 'j', '2'],['1', 'k', '2'],['1', 'l', '2'],['1', 'm', '2'],['1', 'n', '4'],['1', 'o', '2'],['1', 'p', '2'],['1', 'q', '2'],['1', 'r', '2'],['1', 's', '2'],['1', 't', '2'],['1', 'u', '2'],['1', 'v', '2'],['1', 'w', '2'],['1', 'x', '4'],['1', 'y', '2'],['1', 'z', '2'],['1', '0', '3'],['1', '1', '3'],['1', '2', '3'],['1', '3', '3'],['1', '4', '3'],['1', '5', '3'],['1', '6', '3'],['1', '7', '3'],['1', '8', '3'],['1', '9', '3'],['2', 'A', '2'],['2', 'B', '2'],['2', 'C', '2'],['2', 'D', '2'],['2', 'E', '2'],['2', 'F', '2'],['2', 'G', '4'],['2', 'H', '2'],['2', 'I', '2'],['2', 'J', '2'],['2', 'K', '2'],['2', 'L', '2'],['2', 'M', '2'],['2', 'N', '2'],['2', 'O', '2'],['2', 'P', '2'],['2', 'Q', '4'],['2', 'R', '2'],['2', 'S', '2'],['2', 'T', '2'],['2', 'U', '2'],['2', 'V', '2'],['2', 'W', '2'],['2', 'X', '2'],['2', 'Y', '2'],['2', 'Z', '2'],['2', 'a', '4'],['2', 'b', '2'],['2', 'c', '2'],['2', 'd', '2'],['2', 'e', '2'],['2', 'f', '2'],['2', 'g', '2'],['2', 'h', '2'],['2', 'i', '2'],['2', 'j', '2'],['2', 'k', '4'],['2', 'l', '2'],['2', 'm', '2'],['2', 'n', '2'],['2', 'o', '2'],['2', 'p', '2'],['2', 'q', '2'],['2', 'r', '2'],['2', 's', '2'],['2', 't', '4'],['2', 'u', '4'],['2', 'v', '4'],['2', 'w', '4'],['2', 'x', '4'],['2', 'y', '4'],['2', 'z', '4'],['2', '0', '4'],['2', '1', '4'],['2', '2', '4'],['2', '3', '4'],['2', '4', '4'],['2', '5', '4'],['2', '6', '4'],['2', '7', '4'],['2', '8', '4'],['2', '9', '4'],['4', 'A', '2'],['4', 'B', '2'],['4', 'C', '2'],['4', 'D', '2'],['4', 'E', '2'],['4', 'F', '2'],['4', 'G', '4'],['4', 'H', '2'],['4', 'I', '2'],['4', 'J', '2'],['4', 'K', '2'],['4', 'L', '2'],['4', 'M', '2'],['4', 'N', '2'],['4', 'O', '2'],['4', 'P', '2'],['4', 'Q', '4'],['4', 'R', '2'],['4', 'S', '2'],['4', 'T', '2'],['4', 'U', '2'],['4', 'V', '2'],['4', 'W', '2'],['4', 'X', '2'],['4', 'Y', '2'],['4', 'Z', '2'],['4', 'a', '4'],['4', 'b', '2'],['4', 'c', '2'],['4', 'd', '2'],['4', 'e', '2'],['4', 'f', '2'],['4', 'g', '2'],['4', 'h', '2'],['4', 'i', '2'],['4', 'j', '2'],['4', 'k', '4'],['4', 'l', '2'],['4', 'm', '2'],['4', 'n', '2'],['4', 'o', '2'],['4', 'p', '2'],['4', 'q', '2'],['4', 'r', '2'],['4', 's', '2'],['4', 't', '4'],['4', 'u', '4'],['4', 'v', '4'],['4', 'w', '4'],['4', 'x', '4'],['4', 'y', '4'],['4', 'z', '4'],['4', '0', '4'],['4', '1', '4'],['4', '2', '4'],['4', '3', '4'],['4', '4', '4'],['4', '5', '4'],['4', '6', '4'],['4', '7', '4'],['4', '8', '4'],['4', '9', '4'],['3', 'A', '3'],['3', 'B', '3'],['3', 'C', '3'],['3', 'D', '3'],['3', 'E', '3'],['3', 'F', '3'],['3', 'G', '3'],['3', 'H', '3'],['3', 'I', '3'],['3', 'J', '3'],['3', 'K', '3'],['3', 'L', '3'],['3', 'M', '3'],['3', 'N', '3'],['3', 'O', '3'],['3', 'P', '3'],['3', 'Q', '3'],['3', 'R', '3'],['3', 'S', '3'],['3', 'T', '3'],['3', 'U', '3'],['3', 'V', '3'],['3', 'W', '3'],['3', 'X', '3'],['3', 'Y', '3'],['3', 'Z', '3'],['3', 'a', '3'],['3', 'b', '3'],['3', 'c', '3'],['3', 'd', '3'],['3', 'e', '3'],['3', 'f', '3'],['3', 'g', '3'],['3', 'h', '3'],['3', 'i', '3'],['3', 'j', '3'],['3', 'k', '3'],['3', 'l', '3'],['3', 'm', '3'],['3', 'n', '3'],['3', 'o', '3'],['3', 'p', '3'],['3', 'q', '3'],['3', 'r', '3'],['3', 's', '3'],['3', 't', '3'],['3', 'u', '3'],['3', 'v', '3'],['3', 'w', '3'],['3', 'x', '3'],['3', 'y', '3'],['3', 'z', '3'],['3', '0', '3'],['3', '1', '3'],['3', '2', '3'],['3', '3', '3'],['3', '4', '3'],['3', '5', '3'],['3', '6', '3'],['3', '7', '3'],['3', '8', '3'],['3', '9', '3'],['1', 'A', '2'],['1', 'B', '2'],['1', 'C', '2'],['1', 'D', '2'],['1', 'E', '2'],['1', 'F', '2'],['1', 'G', '2'],['1', 'H', '2'],['1', 'I', '4'],['1', 'J', '4'],['1', 'K', '4'],['1', 'L', '4'],['1', 'M', '4'],['1', 'N', '4'],['1', 'O', '4'],['1', 'P', '4'],['1', 'Q', '4'],['1', 'R', '4'],['1', 'S', '2'],['1', 'T', '4'],['1', 'U', '2'],['1', 'V', '2'],['1', 'W', '2'],['1', 'X', '2'],['1', 'Y', '2'],['1', 'Z', '2'],['1', 'a', '2'],['1', 'b', '2'],['1', 'c', '2'],['1', 'd', '4'],['1', 'e', '2'],['1', 'f', '2'],['1', 'g', '2'],['1', 'h', '2'],['1', 'i', '2'],['1', 'j', '2'],['1', 'k', '2'],['1', 'l', '2'],['1', 'm', '2'],['1', 'n', '4'],['1', 'o', '2'],['1', 'p', '2'],['1', 'q', '2'],['1', 'r', '2'],['1', 's', '2'],['1', 't', '2'],['1', 'u', '2'],['1', 'v', '2'],['1', 'w', '2'],['1', 'x', '4'],['1', 'y', '2'],['1', 'z', '2'],['1', '0', '3'],['1', '1', '3'],['1', '2', '3'],['1', '3', '3'],['1', '4', '3'],['1', '5', '3'],['1', '6', '3'],['1', '7', '3'],['1', '8', '3'],['1', '9', '3'],['2', 'A', '2'],['2', 'B', '2'],['2', 'C', '2'],['2', 'D', '2'],['2', 'E', '2'],['2', 'F', '2'],['2', 'G', '4'],['2', 'H', '2'],['2', 'I', '2'],['2', 'J', '2'],['2', 'K', '2'],['2', 'L', '2'],['2', 'M', '2'],['2', 'N', '2'],['2', 'O', '2'],['2', 'P', '2'],['2', 'Q', '4'],['2', 'R', '2'],['2', 'S', '2'],['2', 'T', '2'],['2', 'U', '2'],['2', 'V', '2'],['2', 'W', '2'],['2', 'X', '2'],['2', 'Y', '2'],['2', 'Z', '2'],['2', 'a', '4'],['2', 'b', '2'],['2', 'c', '2'],['2', 'd', '2'],['2', 'e', '2'],['2', 'f', '2'],['2', 'g', '2'],['2', 'h', '2'],['2', 'i', '2'],['2', 'j', '2'],['2', 'k', '4'],['2', 'l', '2'],['2', 'm', '2'],['2', 'n', '2'],['2', 'o', '2'],['2', 'p', '2'],['2', 'q', '2'],['2', 'r', '2'],['2', 's', '2'],['2', 't', '4'],['2', 'u', '4'],['2', 'v', '4'],['2', 'w', '4'],['2', 'x', '4'],['2', 'y', '4'],['2', 'z', '4'],['2', '0', '4'],['2', '1', '4'],['2', '2', '4'],['2', '3', '4'],['2', '4', '4'],['2', '5', '4'],['2', '6', '4'],['2', '7', '4'],['2', '8', '4'],['2', '9', '4'],['4', 'A', '2'],['4', 'B', '2'],['4', 'C', '2'],['4', 'D', '2'],['4', 'E', '2'],['4', 'F', '2'],['4', 'G', '4'],['4', 'H', '2'],['4', 'I', '2'],['4', 'J', '2'],['4', 'K', '2'],['4', 'L', '2'],['4', 'M', '2'],['4', 'N', '2'],['4', 'O', '2'],['4', 'P', '2'],['4', 'Q', '4'],['4', 'R', '2'],['4', 'S', '2'],['4', 'T', '2'],['4', 'U', '2'],['4', 'V', '2'],['4', 'W', '2'],['4', 'X', '2'],['4', 'Y', '2'],['4', 'Z', '2'],['4', 'a', '4'],['4', 'b', '2'],['4', 'c', '2'],['4', 'd', '2'],['4', 'e', '2'],['4', 'f', '2'],['4', 'g', '2'],['4', 'h', '2'],['4', 'i', '2'],['4', 'j', '2'],['4', 'k', '4'],['4', 'l', '2'],['4', 'm', '2'],['4', 'n', '2'],['4', 'o', '2'],['4', 'p', '2'],['4', 'q', '2'],['4', 'r', '2'],['4', 's', '2'],['4', 't', '4'],['4', 'u', '4'],['4', 'v', '4'],['4', 'w', '4'],['4', 'x', '4'],['4', 'y', '4'],['4', 'z', '4'],['4', '0', '4'],['4', '1', '4'],['4', '2', '4'],['4', '3', '4'],['4', '4', '4'],['4', '5', '4'],['4', '6', '4'],['4', '7', '4'],['4', '8', '4'],['4', '9', '4'],['3', 'A', '3'],['3', 'B', '3'],['3', 'C', '3'],['3', 'D', '3'],['3', 'E', '3'],['3', 'F', '3'],['3', 'G', '3'],['3', 'H', '3'],['3', 'I', '3'],['3', 'J', '3'],['3', 'K', '3'],['3', 'L', '3'],['3', 'M', '3'],['3', 'N', '3'],['3', 'O', '3'],['3', 'P', '3'],['3', 'Q', '3'],['3', 'R', '3'],['3', 'S', '3'],['3', 'T', '3'],['3', 'U', '3'],['3', 'V', '3'],['3', 'W', '3'],['3', 'X', '3'],['3', 'Y', '3'],['3', 'Z', '3'],['3', 'a', '3'],['3', 'b', '3'],['3', 'c', '3'],['3', 'd', '3'],['3', 'e', '3'],['3', 'f', '3'],['3', 'g', '3'],['3', 'h', '3'],['3', 'i', '3'],['3', 'j', '3'],['3', 'k', '3'],['3', 'l', '3'],['3', 'm', '3'],['3', 'n', '3'],['3', 'o', '3'],['3', 'p', '3'],['3', 'q', '3'],['3', 'r', '3'],['3', 's', '3'],['3', 't', '3'],['3', 'u', '3'],['3', 'v', '3'],['3', 'w', '3'],['3', 'x', '3'],['3', 'y', '3'],['3', 'z', '3'],['3', '0', '3'],['3', '1', '3'],['3', '2', '3'],['3', '3', '3'],['3', '4', '3'],['3', '5', '3'],['3', '6', '3'],['3', '7', '3'],['3', '8', '3'],['3', '9', '3'],['1', 'A', '2'],['1', 'B', '2'],['1', 'C', '2'],['1', 'D', '2'],['1', 'E', '2'],['1', 'F', '2'],['1', 'G', '2'],['1', 'H', '2'],['1', 'I', '4'],['1', 'J', '4'],['1', 'K', '4'],['1', 'L', '4'],['1', 'M', '4'],['1', 'N', '4'],['1', 'O', '4'],['1', 'P', '4'],['1', 'Q', '4'],['1', 'R', '4'],['1', 'S', '2'],['1', 'T', '4'],['1', 'U', '2'],['1', 'V', '2'],['1', 'W', '2'],['1', 'X', '2'],['1', 'Y', '2'],['1', 'Z', '2'],['1', 'a', '2'],['1', 'b', '2'],['1', 'c', '2'],['1', 'd', '4'],['1', 'e', '2'],['1', 'f', '2'],['1', 'g', '2'],['1', 'h', '2'],['1', 'i', '2'],['1', 'j', '2'],['1', 'k', '2'],['1', 'l', '2'],['1', 'm', '2'],['1', 'n', '4'],['1', 'o', '2'],['1', 'p', '2'],['1', 'q', '2'],['1', 'r', '2'],['1', 's', '2'],['1', 't', '2'],['1', 'u', '2'],['1', 'v', '2'],['1', 'w', '2'],['1', 'x', '4'],['1', 'y', '2'],['1', 'z', '2'],['1', '0', '3'],['1', '1', '3'],['1', '2', '3'],['1', '3', '3'],['1', '4', '3'],['1', '5', '3'],['1', '6', '3'],['1', '7', '3'],['1', '8', '3'],['1', '9', '3'],['2', 'A', '2'],['2', 'B', '2'],['2', 'C', '2'],['2', 'D', '2'],['2', 'E', '2'],['2', 'F', '2'],['2', 'G', '4'],['2', 'H', '2'],['2', 'I', '2'],['2', 'J', '2'],['2', 'K', '2'],['2', 'L', '2'],['2', 'M', '2'],['2', 'N', '2'],['2', 'O', '2'],['2', 'P', '2'],['2', 'Q', '4'],['2', 'R', '2'],['2', 'S', '2'],['2', 'T', '2'],['2', 'U', '2'],['2', 'V', '2'],['2', 'W', '2'],['2', 'X', '2'],['2', 'Y', '2'],['2', 'Z', '2'],['2', 'a', '4'],['2', 'b', '2'],['2', 'c', '2'],['2', 'd', '2'],['2', 'e', '2'],['2', 'f', '2'],['2', 'g', '2'],['2', 'h', '2'],['2', 'i', '2'],['2', 'j', '2'],['2', 'k', '4'],['2', 'l', '2'],['2', 'm', '2'],['2', 'n', '2'],['2', 'o', '2'],['2', 'p', '2'],['2', 'q', '2'],['2', 'r', '2'],['2', 's', '2'],['2', 't', '4'],['2', 'u', '4'],['2', 'v', '4'],['2', 'w', '4'],['2', 'x', '4'],['2', 'y', '4'],['2', 'z', '4'],['2', '0', '4'],['2', '1', '4'],['2', '2', '4'],['2', '3', '4'],['2', '4', '4'],['2', '5', '4'],['2', '6', '4'],['2', '7', '4'],['2', '8', '4'],['2', '9', '4'],['4', 'A', '2'],['4', 'B', '2'],['4', 'C', '2'],['4', 'D', '2'],['4', 'E', '2'],['4', 'F', '2'],['4', 'G', '4'],['4', 'H', '2'],['4', 'I', '2'],['4', 'J', '2'],['4', 'K', '2'],['4', 'L', '2'],['4', 'M', '2'],['4', 'N', '2'],['4', 'O', '2'],['4', 'P', '2'],['4', 'Q', '4'],['4', 'R', '2'],['4', 'S', '2'],['4', 'T', '2'],['4', 'U', '2'],['4', 'V', '2'],['4', 'W', '2'],['4', 'X', '2'],['4', 'Y', '2'],['4', 'Z', '2'],['4', 'a', '4'],['4', 'b', '2'],['4', 'c', '2'],['4', 'd', '2'],['4', 'e', '2'],['4', 'f', '2'],['4', 'g', '2'],['4', 'h', '2'],['4', 'i', '2'],['4', 'j', '2'],['4', 'k', '4'],['4', 'l', '2'],['4', 'm', '2'],['4', 'n', '2'],['4', 'o', '2'],['4', 'p', '2'],['4', 'q', '2'],['4', 'r', '2'],['4', 's', '2'],['4', 't', '4'],['4', 'u', '4'],['4', 'v', '4'],['4', 'w', '4'],['4', 'x', '4'],['4', 'y', '4'],['4', 'z', '4'],['4', '0', '4'],['4', '1', '4'],['4', '2', '4'],['4', '3', '4'],['4', '4', '4'],['4', '5', '4'],['4', '6', '4'],['4', '7', '4'],['4', '8', '4'],['4', '9', '4'],['3', 'A', '3'],['3', 'B', '3'],['3', 'C', '3'],['3', 'D', '3'],['3', 'E', '3'],['3', 'F', '3'],['3', 'G', '3'],['3', 'H', '3'],['3', 'I', '3'],['3', 'J', '3'],['3', 'K', '3'],['3', 'L', '3'],['3', 'M', '3'],['3', 'N', '3'],['3', 'O', '3'],['3', 'P', '3'],['3', 'Q', '3'],['3', 'R', '3'],['3', 'S', '3'],['3', 'T', '3'],['3', 'U', '3'],['3', 'V', '3'],['3', 'W', '3'],['3', 'X', '3'],['3', 'Y', '3'],['3', 'Z', '3'],['3', 'a', '3'],['3', 'b', '3'],['3', 'c', '3'],['3', 'd', '3'],['3', 'e', '3'],['3', 'f', '3'],['3', 'g', '3'],['3', 'h', '3'],['3', 'i', '3'],['3', 'j', '3'],['3', 'k', '3'],['3', 'l', '3'],['3', 'm', '3'],['3', 'n', '3'],['3', 'o', '3'],['3', 'p', '3'],['3', 'q', '3'],['3', 'r', '3'],['3', 's', '3'],['3', 't', '3'],['3', 'u', '3'],['3', 'v', '3'],['3', 'w', '3'],['3', 'x', '3'],['3', 'y', '3'],['3', 'z', '3'],['3', '0', '3'],['3', '1', '3'],['3', '2', '3'],['3', '3', '3'],['3', '4', '3'],['3', '5', '3'],['3', '6', '3'],['3', '7', '3'],['3', '8', '3'],['3', '9', '3'],['1', 'A', '2'],['1', 'B', '2'],['1', 'C', '2'],['1', 'D', '2'],['1', 'E', '2'],['1', 'F', '2'],['1', 'G', '2'],['1', 'H', '2'],['1', 'I', '4'],['1', 'J', '4'],['1', 'K', '4'],['1', 'L', '4'],['1', 'M', '4'],['1', 'N', '4'],['1', 'O', '4'],['1', 'P', '4'],['1', 'Q', '4'],['1', 'R', '4'],['1', 'S', '2'],['1', 'T', '4'],['1', 'U', '2'],['1', 'V', '2'],['1', 'W', '2'],['1', 'X', '2'],['1', 'Y', '2'],['1', 'Z', '2'],['1', 'a', '2'],['1', 'b', '2'],['1', 'c', '2'],['1', 'd', '4'],['1', 'e', '2'],['1', 'f', '2'],['1', 'g', '2'],['1', 'h', '2'],['1', 'i', '2'],['1', 'j', '2'],['1', 'k', '2'],['1', 'l', '2'],['1', 'm', '2'],['1', 'n', '4'],['1', 'o', '2'],['1', 'p', '2'],['1', 'q', '2'],['1', 'r', '2'],['1', 's', '2'],['1', 't', '2'],['1', 'u', '2'],['1', 'v', '2'],['1', 'w', '2'],['1', 'x', '4'],['1', 'y', '2'],['1', 'z', '2'],['1', '0', '3'],['1', '1', '3'],['1', '2', '3'],['1', '3', '3'],['1', '4', '3'],['1', '5', '3'],['1', '6', '3'],['1', '7', '3'],['1', '8', '3'],['1', '9', '3'],['2', 'A', '2'],['2', 'B', '2'],['2', 'C', '2'],['2', 'D', '2'],['2', 'E', '2'],['2', 'F', '2'],['2', 'G', '4'],['2', 'H', '2'],['2', 'I', '2'],['2', 'J', '2'],['2', 'K', '2'],['2', 'L', '2'],['2', 'M', '2'],['2', 'N', '2'],['2', 'O', '2'],['2', 'P', '2'],['2', 'Q', '4'],['2', 'R', '2'],['2', 'S', '2'],['2', 'T', '2'],['2', 'U', '2'],['2', 'V', '2'],['2', 'W', '2'],['2', 'X', '2'],['2', 'Y', '2'],['2', 'Z', '2'],['2', 'a', '4'],['2', 'b', '2'],['2', 'c', '2'],['2', 'd', '2'],['2', 'e', '2'],['2', 'f', '2'],['2', 'g', '2'],['2', 'h', '2'],['2', 'i', '2'],['2', 'j', '2'],['2', 'k', '4'],['2', 'l', '2'],['2', 'm', '2'],['2', 'n', '2'],['2', 'o', '2'],['2', 'p', '2'],['2', 'q', '2'],['2', 'r', '2'],['2', 's', '2'],['2', 't', '4'],['2', 'u', '4'],['2', 'v', '4'],['2', 'w', '4'],['2', 'x', '4'],['2', 'y', '4'],['2', 'z', '4'],['2', '0', '4'],['2', '1', '4'],['2', '2', '4'],['2', '3', '4'],['2', '4', '4'],['2', '5', '4'],['2', '6', '4'],['2', '7', '4'],['2', '8', '4'],['2', '9', '4'],['4', 'A', '2'],['4', 'B', '2'],['4', 'C', '2'],['4', 'D', '2'],['4', 'E', '2'],['4', 'F', '2'],['4', 'G', '4'],['4', 'H', '2'],['4', 'I', '2'],['4', 'J', '2'],['4', 'K', '2'],['4', 'L', '2'],['4', 'M', '2'],['4', 'N', '2'],['4', 'O', '2'],['4', 'P', '2'],['4', 'Q', '4'],['4', 'R', '2'],['4', 'S', '2'],['4', 'T', '2'],['4', 'U', '2'],['4', 'V', '2'],['4', 'W', '2'],['4', 'X', '2'],['4', 'Y', '2'],['4', 'Z', '2'],['4', 'a', '4'],['4', 'b', '2'],['4', 'c', '2'],['4', 'd', '2'],['4', 'e', '2'],['4', 'f', '2'],['4', 'g', '2'],['4', 'h', '2'],['4', 'i', '2'],['4', 'j', '2'],['4', 'k', '4'],['4', 'l', '2'],['4', 'm', '2'],['4', 'n', '2'],['4', 'o', '2'],['4', 'p', '2'],['4', 'q', '2'],['4', 'r', '2'],['4', 's', '2'],['4', 't', '4'],['4', 'u', '4'],['4', 'v', '4'],['4', 'w', '4'],['4', 'x', '4'],['4', 'y', '4'],['4', 'z', '4'],['4', '0', '4'],['4', '1', '4'],['4', '2', '4'],['4', '3', '4'],['4', '4', '4'],['4', '5', '4'],['4', '6', '4'],['4', '7', '4'],['4', '8', '4'],['4', '9', '4'],['3', 'A', '3'],['3', 'B', '3'],['3', 'C', '3'],['3', 'D', '3'],['3', 'E', '3'],['3', 'F', '3'],['3', 'G', '3'],['3', 'H', '3'],['3', 'I', '3'],['3', 'J', '3'],['3', 'K', '3'],['3', 'L', '3'],['3', 'M', '3'],['3', 'N', '3'],['3', 'O', '3'],['3', 'P', '3'],['3', 'Q', '3'],['3', 'R', '3'],['3', 'S', '3'],['3', 'T', '3'],['3', 'U', '3'],['3', 'V', '3'],['3', 'W', '3'],['3', 'X', '3'],['3', 'Y', '3'],['3', 'Z', '3'],['3', 'a', '3'],['3', 'b', '3'],['3', 'c', '3'],['3', 'd', '3'],['3', 'e', '3'],['3', 'f', '3'],['3', 'g', '3'],['3', 'h', '3'],['3', 'i', '3'],['3', 'j', '3'],['3', 'k', '3'],['3', 'l', '3'],['3', 'm', '3'],['3', 'n', '3'],['3', 'o', '3'],['3', 'p', '3'],['3', 'q', '3'],['3', 'r', '3'],['3', 's', '3'],['3', 't', '3'],['3', 'u', '3'],['3', 'v', '3'],['3', 'w', '3'],['3', 'x', '3'],['3', 'y', '3'],['3', 'z', '3'],['3', '0', '3'],['3', '1', '3'],['3', '2', '3'],['3', '3', '3'],['3', '4', '3'],['3', '5', '3'],['3', '6', '3'],['3', '7', '3'],['3', '8', '3'],['3', '9', '3'],['0', 'ε', '5'],['5', '0', '6'],['5', '1', '6'],['5', '2', '6'],['5', '3', '6'],['5', '4', '6'],['5', '5', '6'],['5', '6', '6'],['5', '7', '6'],['5', '8', '6'],['5', '9', '6'],['6', '0', '6'],['6', '1', '6'],['6', '2', '6'],['6', '3', '6'],['6', '4', '6'],['6', '5', '6'],['6', '6', '6'],['6', '7', '6'],['6', '8', '6'],['6', '9', '6'],['5', '0', '6'],['5', '1', '6'],['5', '2', '6'],['5', '3', '6'],['5', '4', '6'],['5', '5', '6'],['5', '6', '6'],['5', '7', '6'],['5', '8', '6'],['5', '9', '6'],['6', '0', '6'],['6', '1', '6'],['6', '2', '6'],['6', '3', '6'],['6', '4', '6'],['6', '5', '6'],['6', '6', '6'],['6', '7', '6'],['6', '8', '6'],['6', '9', '6']],['0'],['2', '4', '6'])
tokenList = [['0', '2'],['0', '4'],['1', '6']]
tokens = [['ident', '(A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z){(A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)|(0|1|2|3|4|5|6|7|8|9)}'],['number', '(0|1|2|3|4|5|6|7|8|9){(0|1|2|3|4|5|6|7|8|9)}']]
keys = [['while', 'while'],['do', 'do'],['if', 'if'],['switch', 'switch']]

keyValues = []
for key in keys:
    keyValues.append(key[1])

testFileName = input("Ingrese el nombre del archivo: ")
file = open(testFileName, "r")
lines = file.readlines()

for line in lines:
    response = (afnSimulator2(combinedAF,line, keyValues))

    cont = 0
    for item in response:
        for t in tokenList:
            if (item == t[1]):
                response[cont] = tokens[int(t[0])][0]
        
        cont += 1

    print(response)
