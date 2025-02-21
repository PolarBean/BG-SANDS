from openminds import Collection,IRI
from openminds.latest import sands, controlled_terms
import openminds.latest.core as omcore
import brainglobe_atlasapi

# Create the CommonCoordinateSpace instance
"""
For brainglobe purposes I am treating Common Coordinate Space more like
a Common Coordinate Framework which is not yet represented in openminds

"""
ccfv3 = sands.CommonCoordinateSpace(
    id="_:allen_ccfv3_coordinate_space",
    abbreviation="CCFv3",
    description="The 'Allen Mouse Brain Common Coordinate Framework Version 3' is a 3D reconstruction of an averaged adult mouse brain.",
    full_name="Allen Mouse Brain Common Coordinate Framework Version 3",
    homepage="https://portal.brain-map.org/",
    short_name="Allen Mouse Brain CCF",
    used_species=controlled_terms.species.Species.mus_musculus,
    has_versions=[],
)

# Create the CommonCoordinateSpaceVersion instance
"""
I am also doing this differently than openminds. Each Common Coordinate Space
version is really a different atlas release that involves a new template.
That's because in openminds whenever the template changes the Common Coordinate
Space Version changes, but a Common Coordinate Space version can have multiple
default images. I think the image that is considered the main one should go first.
"""
allen_stpt_ccfv3 = sands.CommonCoordinateSpaceVersion(
    id="_:allen_ccfv3_stpt",
    abbreviation="allen_ccfv3",
    accessibility=controlled_terms.product_accessibility.ProductAccessibility.free_access,
    anatomical_axes_orientation=controlled_terms.anatomical_axes_orientation.AnatomicalAxesOrientation.pir,
    axes_origins=[
        omcore.QuantitativeValue(value=0.0),
        omcore.QuantitativeValue(value=0.0),
        omcore.QuantitativeValue(value=0.0),
    ],
    default_images=[],
    full_name="Allen Mouse Brain Common Coordinate Framework version 3",
    homepage="https://portal.brain-map.org/",
    how_to_cite="Wang Q, Ding S-L, Li Y, et al.; 'The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas.'; Cell; May 2020; 181(4):936-953.e20. [doi: 10.1016/j.cell.2020.04.007](https://doi.org/10.1016/j.cell.2020.04.007)",
    native_unit=controlled_terms.unit_of_measurement.UnitOfMeasurement.micrometer,
    release_date="2015-05-01",
    short_name="Allen Mouse Brain CCF",
    version_identifier="v3",
    version_innovation="The third version of the 'Allen Mouse Brain Common Coordinate Framework' (CCFv3) is a 3D reconstruction of a whole brain at 10µm resolution.",
    related_publications=[IRI("https://doi.org/10.1016/j.cell.2020.04.007")],
)



# Additional metadata
allen_stpt_ccfv3.bg_name = "allen_mouse"
allen_stpt_ccfv3.atlas_link = "http://www.brain-map.org"
allen_stpt_ccfv3.species = "Mus musculus"
allen_stpt_ccfv3.symmetric = True
allen_stpt_ccfv3.resolution = [10.0, 10.0, 10.0]
allen_stpt_ccfv3.orientation = "asr"
allen_stpt_ccfv3.__bgversion__ = "1.2"
allen_stpt_ccfv3.shape = [1320, 800, 1140]
allen_stpt_ccfv3.transform_to_bg = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0],
]
allen_stpt_ccfv3.additional_references = []
ccfv3.has_versions.append(allen_stpt_ccfv3)
#wrapup
collection = Collection()
collection.add(ccfv3, allen_stpt_ccfv3)
errors = collection.validate()
print(errors)
collection.save("../metadata", individual_files=True)

