func mergeAlternately(word1 string, word2 string) string {
	len1 := len(word1)
	len2 := len(word2)
	min_len := min(len1, len2)
	var result string
	for i := 0; i < min_len; i++ {
		result += string(word1[i]) + string(word2[i])
	}

	return result + word1[min_len:] + word2[min_len:]
}