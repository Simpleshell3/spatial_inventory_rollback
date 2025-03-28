select
disturbance_type.name disturbance_type_name,
disturbance_matrix_association.disturbance_matrix_id,
disturbance_matrix_association.spatial_unit_id,
pool_src.name pool_name,
sum(disturbance_matrix_value.proportion) proportion_lost
from disturbance_matrix_association inner join disturbance_type
	on disturbance_matrix_association.disturbance_type_id
		== disturbance_type.id
inner join disturbance_matrix_value
	on disturbance_matrix_association.disturbance_matrix_id
		== disturbance_matrix_value.disturbance_matrix_id
inner join pool pool_src
	on disturbance_matrix_value.source_pool_id == pool_src.id
inner join pool pool_sink
	on disturbance_matrix_value.sink_pool_id == pool_sink.id
where pool_src.name in (
		'SoftwoodMerch','SoftwoodFoliage','SoftwoodOther',
		'SoftwoodCoarseRoots','SoftwoodFineRoots',
		'HardwoodMerch','HardwoodFoliage','HardwoodOther',
		'HardwoodCoarseRoots','HardwoodFineRoots') and
	pool_sink.name not in(
		'SoftwoodMerch','SoftwoodFoliage','SoftwoodOther',
		'SoftwoodCoarseRoots','SoftwoodFineRoots',
		'HardwoodMerch','HardwoodFoliage','HardwoodOther',
		'HardwoodCoarseRoots','HardwoodFineRoots')
group by
disturbance_type.name,
disturbance_matrix_association.disturbance_matrix_id,
disturbance_matrix_association.spatial_unit_id,
pool_src.name
