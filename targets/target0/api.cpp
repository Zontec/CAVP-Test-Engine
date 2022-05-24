#include "api.hpp"

TEST_API uint32_t sha1(uint8_t *data, uint32_t len, uint8_t *hash) {
    return mbcrypt_sha1(data, len / 8, hash);
}

TEST_API uint32_t sha256(uint8_t *data, uint32_t len, uint8_t *hash) {
    return mbcrypt_sha256(data, len / 8, hash);
}

TEST_API uint32_t sha512(uint8_t *data, uint32_t len, uint8_t *hash) {
    return mbcrypt_sha512(data, len / 8, hash);
}
