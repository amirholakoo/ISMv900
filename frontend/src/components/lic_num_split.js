export function parseLicenseNumber(licenseNumber) {
    // Assuming the pattern is consistent
    const first = licenseNumber.slice(0, 2);
    const letter = licenseNumber.slice(2, 3);
    const second = licenseNumber.slice(5, 6);
    const year = licenseNumber.slice(-2);

    // Create an object with the parsed values
    return {
        first: first,
        letter: letter,
        second: second,
        country: 'ایران',
        year: year
    };
}
export function LicenseNumberParser(licenseNumber) {
    // Define a regex pattern to match the parts of the license number, including line breaks
    const regex = /^(\d{2})(\w)(\d{3})(\w{5})(\d{2})$/;
    const matches = licenseNumber.match(regex);

    if (matches) {
        console.log(matches)
        // Extract the matched groups
        const first = matches[1];
        const letter = matches[2];
        const second = matches[3];
        const year = matches[5];

        // Create an object with the parsed values
        return {
            first: first,
            letter: letter,
            second: second,
            country: 'ایران',
            year: year
        }
    }
}
