const str = "AABBACCDDBDE";
const freqMap = new Map();

for (let char of str) {
  freqMap.set(char, (freqMap.get(char) || 0) + 1);
}

// Output: Map(5) { 'A' => 3, 'B' => 3, 'C' => 2, 'D' => 3, 'E' => 1 }
console.log(freqMap);
