from apistar import typesystem

class ExcludeCharacters(typesystem.String):
	description = "characters to exclude from the randomly generated string."
	max_length = 10
	trim_whitespace = True
	default = []

class StringLength(typesystem.Integer):
	description = "the length of the randomly generated string."
	default = 16
	maximum = 64
	minimum = 12

class IncludeAlpha(typesystem.Boolean):
	description = "Include alpha characters in the randomly generated string."
	default = True

class IncludeDigit(typesystem.Boolean):
	description = "Include digit characters in the randomly generated string."
	default = True

class IncludePunctuation(typesystem.Boolean):
	description = "Include punctuation characters in the randomly generated string."
	default = True

class ForceUpper(typesystem.Boolean):
	description = "Generate an uppercase random string."
	default = False

class ForceLower(typesystem.Boolean):
	description = "Generate a lowerclass random string."
	default = False

class StringRequest(typesystem.Object):
	properties = {
		"exclude": ExcludeCharacters, 
		"length": StringLength,
		"alpha": IncludeAlpha,
		"digit": IncludeDigit,
		"punctuation": IncludePunctuation,
		"upper": ForceUpper,
		"lower": ForceLower
	}
