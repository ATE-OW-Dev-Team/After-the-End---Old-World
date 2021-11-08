#ifndef CONSTANTS_H_
#define CONSTANTS_H_

// --------------------------------------------------------------
// ------------------    Light          -------------------------
// --------------------------------------------------------------
static const float3 LIGHT_DIFFUSE				= float3( 1.0f, 1.0f, 1.0f );// Not used anymore
static const float  LIGHT_INTENSITY   			= 4.0f;
static const float3  AMBIENT					= float3( 0.03f, 0.05f, 0.07f );
static const float3 MAP_LIGHT_DIFFUSE			= float3( 1.0f, 1.0f, 1.0f );// Not used anymore
static const float  MAP_LIGHT_INTENSITY   		= 2.5f;
static const float3  MAP_AMBIENT				= float3( 0.03f, 0.05f, 0.07f );
static const float	LIGHT_HDR_RANGE 			= 0.8f;

// --------------------------------------------------------------
// ------------------    TERRAIN        -------------------------
// --------------------------------------------------------------

static const float TREE_SEASON_MIN 			= 0.5f;
static const float TREE_SEASON_FADE_TWEAK 	= 2.5f;

#endif //CONSTANTS_H_