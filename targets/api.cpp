#include "api.hpp"

#define TEST_API extern "C"

/* Your declarations starts from here */

TEST_API uint32_t sha1(uint8_t *data, uint32_t len, uint8_t *hash) {
    /* Your code is here */
    return 0;
}

TEST_API uint32_t sha256(uint8_t *data, uint32_t len, uint8_t *hash) {
    /* Your code is here */
    return 0;
}

TEST_API uint32_t sha512(uint8_t *data, uint32_t len, uint8_t *hash) {
    /* Your code is here */
    return 0;
}

TEST_API uint32_t hmac_sha1(uint8_t *key, uint32_t key_len, 
                                uint8_t *data, uint32_t len, uint8_t *hash) {
    /* Your code is here */
    return 0;
}

TEST_API uint32_t hmac_sha256(uint8_t *key, uint32_t key_len, 
                                uint8_t *data, uint32_t len, uint8_t *hash) {
    /* Your code is here */
    return 0;
}

TEST_API uint32_t hmac_sha512(uint8_t *key, uint32_t key_len, 
                                uint8_t *data, uint32_t len, uint8_t *hash) {
    /* Your code is here */
    return 0;
}