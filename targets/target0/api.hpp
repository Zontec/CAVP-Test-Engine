#pragma once

#include <string>
#include <inttypes.h>

#define TEST_API extern "C"

/* You can you can include your headers hear */

extern "C" uint32_t mbcrypt_sha1(uint8_t *data, uint32_t len, uint8_t *hash);
extern "C" uint32_t mbcrypt_sha256(uint8_t *data, uint32_t len, uint8_t *hash);
extern "C" uint32_t mbcrypt_sha512(uint8_t *data, uint32_t len, uint8_t *hash);
